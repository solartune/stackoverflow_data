from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import logout

import requests

from .utils import pagination
from .forms import UserForm

PROVIDER = 'stackoverflow'
POSTS_PER_PAGE = 12


class HomeView(FormMixin, TemplateView):
    template_name = 'core/home.html'
    form_class = UserForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.user_id = form.cleaned_data.get('user_id')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('post_list', kwargs={'user_id': self.user_id})


class LogoutRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            social_user = self.request.user.social_auth \
                .filter(provider=PROVIDER).first()
            if not social_user:
                logout(self.request)

        return reverse('social:begin', args=[PROVIDER])


class PostListView(TemplateView):
    template_name = 'core/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get("page", 1)
        user_id = kwargs.get('user_id')

        url = 'https://api.stackexchange.com/2.2/users/{0}/posts' \
              .format(user_id)
        params = {'site': PROVIDER, 'sort': 'creation', 'order': 'desc'}
        response = requests.get(url, params=params)
        posts = response.json()['items']
        context['posts'] = pagination(
            queryset=posts, per_page=POSTS_PER_PAGE, page=page)
        return context


class MyPostListView(TemplateView):
    template_name = 'core/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get("page", 1)
        user = self.request.user
        if not user.is_authenticated() or not user.social_auth:
            return context

        social_user = user.social_auth.filter(provider=PROVIDER).first()
        if not social_user:
            return context

        access_token = social_user.extra_data.get('access_token')
        if not access_token:
            return context

        url = 'https://api.stackexchange.com/2.2/me/posts'
        params = {
            'site': PROVIDER, 'access_token': access_token,
            'key': settings.SOCIAL_AUTH_STACKOVERFLOW_API_KEY
        }
        response = requests.get(url, params=params)
        posts = response.json()
        response = requests.get(url, params=params)
        posts = response.json()['items']
        context['posts'] = pagination(
            queryset=posts, per_page=POSTS_PER_PAGE, page=page)
        return context
