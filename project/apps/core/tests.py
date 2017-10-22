from unittest.mock import Mock, patch

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User

from .views import LogoutRedirectView
from .constants import (
    PROVIDER, POSTS_PER_PAGE, POSTS_NOT_FOUND_ERROR, CONNECTION_ERROR)


class HomeViewTest(TestCase):

    def setUp(self):
        self.url = reverse('home')

    def test_page_is_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_page_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_form_errors(self):
        response = self.client.post(self.url, {})
        self.assertFormError(
            response, 'form', 'user_id', 'This field is required.')

        response = self.client.post(self.url, {'user_id': 'sd'})
        self.assertFormError(
            response, 'form', 'user_id', 'Enter a whole number.')

    def test_redirect_if_form_is_correct(self):
        user_id = 35
        response = self.client.post(self.url, {'user_id': user_id})
        new_url = reverse('post_list', args=[user_id])
        self.assertRedirects(response, new_url)


class LogoutRedirectViewTest(TestCase):

    def setUp(self):
        self.url = reverse('logout_redirect')
        self.user = User.objects.create_user(
            username='user1', password='secret_pass')

    def test_redirect_is_ok(self):
        # self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class PostListViewTest(TestCase):

    def setUp(self):
        self.user_id = 35
        self.url = reverse('post_list', args=[self.user_id])

    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('project.apps.core.views.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_page_is_ok(self):
        self.mock_get.return_value.ok = True
        self.mock_get.return_value = Mock()
        items = {'items': []}
        self.mock_get.return_value.json.return_value = items
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_page_template(self):
        self.mock_get.return_value.ok = True
        self.mock_get.return_value = Mock()
        posts = {'items': []}
        self.mock_get.return_value.json.return_value = posts
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'core/post_list.html')

    def test_context(self):
        self.mock_get.return_value.ok = True

        posts = {
            "items": [
                {
                    "owner": {
                        "reputation": 15681,
                        "user_id": 34,
                        "display_name": "Karl Seguin",
                        "link": "https://stackoverflow.com/users/34/karl-seguin"
                    },
                    "score": 1,
                    "creation_date": 1326706105,
                    "post_type": "answer",
                    "link": "https://stackoverflow.com/a/8877930"
                },
                {
                    "owner": {
                        "reputation": 15681,
                        "user_id": 34,
                        "display_name": "Karl Seguin",
                        "link": "https://stackoverflow.com/users/34/karl-seguin"
                    },
                    "score": 15,
                    "creation_date": 1293721307,
                    "post_type": "answer",
                    "link": "https://stackoverflow.com/a/4563635"
                }
            ],
        }

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = posts

        response = self.client.get(self.url)

        self.assertEqual(
            len(response.context['posts'].object_list), len(posts['items']))

        self.assertEqual(
            response.context['posts'].object_list[0]['owner']['display_name'],
            posts['items'][0]['owner']['display_name']
        )

    def test_context_for_empty_result(self):
        def test_context(self):
            self.mock_get.return_value.ok = True
            posts = {"items": []}
            self.mock_get.return_value = Mock()
            self.mock_get.return_value.json.return_value = posts

            response = self.client.get(self.url)

            self.assertEqual(response.context['error'], POSTS_NOT_FOUND_ERROR)

    def test_context_for_connection_error(self):
        def test_context_for_empty_result(self):
            self.mock_get.return_value.ok = False
            response = self.client.get(self.url)

            self.assertEqual(response.context['error'], CONNECTION_ERROR)
