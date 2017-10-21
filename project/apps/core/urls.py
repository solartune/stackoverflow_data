from django.conf.urls import url

from project.apps.core.views import HomeView, PostListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(
        r'^user/(?P<user_id>[0-9]+)/posts/$',
        PostListView.as_view(), name='post_list'
    ),


]
