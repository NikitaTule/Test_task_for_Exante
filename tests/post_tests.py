import pytest
from Base.Basic_API_methods import BaseMetods


class TestsPost:

    @pytest.fixture
    def preconditions(self, api_client, base_url):
        return api_client, base_url

    @pytest.fixture
    def postconditions(self, preconditions):
        api_client, base_url = preconditions

        # Метод для удаления пользователя или другой созданой информации
        def _delete_resource(resource_type, resource_id):
            status_code, response = BaseMetods.send_delete_request(base_url, f"{resource_type}/{resource_id}")
            assert status_code == 200

        return _delete_resource

    def test_create_user(self, preconditions, postconditions):
        api_client, base_url = preconditions

        # Подготовка данных для создания нового пользователя
        user_data = {
            'name': 'TEST',
            'username': 'TEST',
            'email': 'TEST@example.com'
        }

        # Отправка POST запроса для создания пользователя с использованием статического метода
        status_code, response = BaseMetods.send_post_request(f"{base_url}", "users", user_data)

        # Проверка, что ответ имеет статус-код 201 (успешное создание)

        assert status_code == 201

        # Сохраняем ID созданного пользователя
        created_user_id = response['id']
        # Проверяем что id пользователя создано
        assert created_user_id is not None
        """ 
        В данном случаи хорошо было бы проверить, что пользователь сохраняется в общем списке пользователей
        но особенность данного апи сделать этого не позволяет, так же как и удалить пользователя после его создания.
        В другом случаи был бы использован код ниже.
        """
        # status_code, all_users = BaseMetods.send_get_request(base_url, "users")
        # assert any(user['id'] == created_user_id for user in all_users)
        # Удаление созданного пользователя с использованием фикстуры postconditions
        # postconditions("users", created_user_id)

    def test_create_post(self, preconditions, postconditions):
        api_client, base_url = preconditions

        # Подготовка данных для создания нового поста
        post_data = {
            'userId': 1,
            'title': 'New Post',
            'body': 'This is the body of the new post.'
        }

        # Отправка POST запроса для создания поста
        status_code, response = BaseMetods.send_post_request(f"{base_url}", "posts", post_data)

        # Проверка, что ответ имеет статус-код 201 (успешное создание)
        assert status_code == 201

        # Проверка, что ID созданного поста создано
        created_post_id = response.get('id')
        assert created_post_id is not None
        """
        Как я писал выше данное апи не позволяет в полной мере проверить,
        что пост создан получая title  всех постов
        или очищать после себя удаляя созданный комментарий кодом ниже.
        """
        # Удаление созданного поста с использованием фикстуры postconditions
        # postconditions("posts", created_post_id)

    def test_create_comment(self, preconditions, postconditions):
        api_client, base_url = preconditions

        # Подготовка данных для создания нового комментария
        comment_data = {
            'postId': 1,
            'name': 'New Comment',
            'email': 'newcomment@example.com',
            'body': 'This is the body of the new comment.'
        }

        # Отправка POST запроса для создания комментария
        status_code, response = BaseMetods.send_post_request(f"{base_url}", "comments", comment_data)

        # Проверка, что ответ имеет статус-код 201 (успешное создание)
        assert status_code == 201

        # Проверка, что ID созданного комментария совпадает с ожидаемым
        created_comment_id = response.get('id')
        assert created_comment_id is not None
        assert created_comment_id == 1  # Проверяем что id который мы передаем в comment_data совпадает с получаемым
        """
        Как я писал выше данное апи не позволяет в полной мере проверить,
        что комментарий создан получая id всех комментариев
        или очищать после себя удаляя созданный комментарий кодом ниже.
        """
        # Удаление созданного комментария с использованием фикстуры postconditions
        postconditions("comments", created_comment_id)