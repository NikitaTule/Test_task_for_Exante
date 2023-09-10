from Base.Basic_API_methods import BaseMetods


def test_get_user(base_url):
    """
    Проверяет, что статус-код ответа равен 200 (успешный запрос).
    Проверяет, что данные о пользователе в ответе соответствуют ожидаемым значениям,
    а именно, что id равно 1 и username равно 'Bret'.
    """
    url = base_url
    response = BaseMetods().send_get_request(url, "users/1")
    assert response["id"] == 1
    assert response["username"] == 'Bret'


def test_get_posts(base_url):
    """
    Проверяет, что статус-код ответа равен 200 (успешный запрос).
    Проверяет, что в ответе есть посты, путем проверки, что длина списка постов больше нуля.
    """
    url = base_url
    response = BaseMetods.send_get_request(url, "posts?userId=1")
    assert len(response) > 0


def test_get_comments(base_url):
    """
    Проверяет, что статус-код ответа равен 200 (успешный запрос).
    Проверяет, что в ответе есть комментарии, путем проверки, что длина списка комментариев больше нуля.
    """
    url = base_url
    response = BaseMetods.send_get_request(url, "comments?postId=1")
    assert len(response) > 0
