from tests.base import BaseCase
from urllib.parse import urljoin
import requests
import pytest


class TestApi(BaseCase):
    def test_get_posts_count(self):
        post_url = urljoin(self.config.URL, 'posts')
        post_list = requests.get(post_url).json()
        filtered = [u for u in post_list if u['userId'] == 2]
        assert len(filtered) == 10

    def test_post_posts(self):
        post_url = urljoin(self.config.URL, 'posts')
        assert requests.post(post_url, data={
            "userId": 1001,
            "title": "test",
            "body": "test work test work"
        }).status_code == 201
