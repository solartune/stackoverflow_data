from django.conf.urls import url

from project.apps.core.views import (
    HomeView, PostListView, OAuthPostListView, LogoutRedirectView)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(
        r'^user/(?P<user_id>[0-9]+)/posts/$',
        PostListView.as_view(), name='post_list'
    ),
    url(
        r'^user/me/posts/$',
        OAuthPostListView.as_view(),
        name='oauth_post_list'
    ),
    url(r'^redirect/$', LogoutRedirectView.as_view(), name='logout_redirect'),

]
