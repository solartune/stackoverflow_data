PROVIDER = 'stackoverflow'

POSTS_PER_PAGE = 12

POSTS_NOT_FOUND_ERROR = {
    'icon': 'frown',
    'caption': 'Posts not found',
    'message': """Unfortunately we didn't find any posts
    for this user."""
}

CONNECTION_ERROR = {
    'icon': 'plug',
    'caption': 'Connection error',
    'message': """Sorry, but we have problems with connection to
    an external service."""
}

TEST_DATA = {
        "items": [
            {
                "owner": {
                    "reputation": 15681,
                    "user_id": 34,
                    "display_name": "Test user name",
                    "link": "https://stackoverflow.com/users/34/test-user-name"
                },
                "score": 1,
                "creation_date": 1326706105,
                "post_type": "answer",
                "link": "https://stackoverflow.com/a/123"
            },
            {
                "owner": {
                    "reputation": 15681,
                    "user_id": 34,
                    "display_name": "Test user name",
                    "link": "https://stackoverflow.com/users/34/test-user-name"
                },
                "score": 15,
                "creation_date": 1293721307,
                "post_type": "answer",
                "link": "https://stackoverflow.com/a/1234"
            }
        ],
    }
