import pytest
from Base.Basic_API_methods import BaseMetods


class TestsGet:

    @pytest.fixture
    def setup(self, base_url):
        self.base_url = base_url

    def test_get_user(self, setup):
        """
        Проверяет, что статус-код ответа равен 200 (успешный запрос).
        Проверяет, что данные о пользователе в ответе соответствуют ожидаемым значениям,
        а именно, что id равно 1 и username равно 'Bret'.
        """
        response = BaseMetods().send_get_request(self.base_url, "users/1")
        assert response["id"] == 1
        assert response["username"] == 'Bret'

    def test_get_posts(self, setup):
        """
        Проверяет, что статус-код ответа равен 200 (успешный запрос).
        Проверяет, что в ответе есть посты, путем проверки, что длина списка постов больше нуля.
        """
        response = BaseMetods.send_get_request(self.base_url, "posts?userId=1")
        assert len(response) > 0

    def test_get_comments(self, setup):
        """
        Проверяет, что статус-код ответа равен 200 (успешный запрос).
        Проверяет, что в ответе есть комментарии, путем проверки, что длина списка комментариев больше нуля.
        """
        response = BaseMetods.send_get_request(self.base_url, "comments?postId=1")
        assert len(response) > 0
