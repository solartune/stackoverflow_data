from django.views.generic import TemplateView, ListView

import requests

from .utils import pagination


class HomeView(TemplateView):
    template_name = 'core/home.html'


class PostListView(TemplateView):
    template_name = 'core/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # import logging
        # logger = logging.getLogger('backend')
        user_id = kwargs.get('user_id')
        url = 'https://api.stackexchange.com/2.2/users/{0}/posts' \
              .format(user_id)
        params = {'site': 'stackoverflow', 'sort': 'creation', 'order': 'desc'}
        response = requests.get(url, params=params)
        posts = response.json()['items']
        page = self.request.GET.get("page", 1)

        context['posts'] = pagination(
            queryset=posts,
            per_page=12,
            page=page
        )

        return context
