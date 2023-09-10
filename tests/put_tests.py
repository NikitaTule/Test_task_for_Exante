import pytest
from Base.Basic_API_methods import BaseMetods


class TestsPut:

    @pytest.fixture
    def preconditions(self, base_url):
        self.base_url = base_url

    def test_update_user(self, preconditions):
        # Подготовка данных для обновления существующего пользователя
        user_data = {
            'id': 1,
            'name': 'Updated Name',
            'username': 'updated_username',
            'email': 'updated_email@example.com'
        }

        # Отправка PUT запроса для обновления пользователя
        status_code, response = BaseMetods.send_put_request(f"{self.base_url}", f"users/{user_data['id']}", user_data)
        print(response)
        # Проверка, что ответ имеет статус-код 200 (успешное обновление)
        assert status_code == 200
        """
        Этот код ниже можно было не писать и использовать закоментированый код ниже, 
        но особенности апи не позволяют, корректно провести проверку
        """
        assert response['name'] == user_data['name']
        assert response['username'] == user_data['username']
        assert response['email'] == user_data['email']

        """
        В данном случаи особенности апи не позволяют проверить, что данные действительно были обновлены кодом ниже
        """
        # Получение обновленных данных пользователя
        # updated_user_data = BaseMetods.send_get_request(self.base_url, f"users/{user_data['id']}")[1]

        # Проверка, что данные пользователя были успешно обновлены
        # assert updated_user_data['name'] == user_data['name']
        # assert updated_user_data['username'] == user_data['username']
        # assert updated_user_data['email'] == user_data['email']

    def test_update_post(self, preconditions):
        # Подготовка данных для обновления существующего поста
        post_data = {
            'id': 1,
            'userId': 1,
            'title': 'Updated Post Title',
            'body': 'Updated body of the post.'
        }

        # Отправка PUT запроса для обновления поста
        status_code, response = BaseMetods.send_put_request(f"{self.base_url}", f"posts/{post_data['id']}", post_data)

        # Проверка, что ответ имеет статус-код 200 (успешное обновление)
        assert status_code == 200

        assert response['title'] == post_data['title']
        assert response['body'] == post_data['body']
        """
        В данном случаи особенности апи не позволяют проверить, что данные действительно были обновлены кодом ниже
        """

        # Получение обновленных данных поста
        # updated_post_data = BaseMetods.send_get_request(self.base_url, f"posts/{post_data['id']}")[1]

        # Проверка, что данные поста были успешно обновлены
        # assert updated_post_data['title'] == post_data['title']
        # assert updated_post_data['body'] == post_data['body']

    def test_update_comment(self, preconditions):
        # Подготовка данных для обновления существующего комментария
        comment_data = {
            'id': 1,
            'postId': 1,
            'name': 'Updated Comment Name',
            'email': 'updated_comment@example.com',
            'body': 'Updated body of the comment.'
        }

        # Отправка PUT запроса для обновления комментария
        status_code, response = BaseMetods.send_put_request(f"{self.base_url}", f"comments/{comment_data['id']}",
                                                            comment_data)

        # Проверка, что ответ имеет статус-код 200 (успешное обновление)
        assert status_code == 200

        assert response['name'] == comment_data['name']
        assert response['email'] == comment_data['email']
        assert response['body'] == comment_data['body']
        """
        В данном случаи особенности апи не позволяют проверить, что данные действительно были обновлены кодом ниже
        """
        # Получение обновленных данных комментария
        # updated_comment_data = BaseMetods.send_get_request(self.base_url, f"comments/{comment_data['id']}")[1]

        # Проверка, что данные комментария были успешно обновлены
        # assert updated_comment_data['name'] == comment_data['name']
        # assert updated_comment_data['email'] == comment_data['email']
        # assert updated_comment_data['body'] == comment_data['body']
