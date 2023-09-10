import pytest
import requests


@pytest.fixture(scope="function")
def base_url():
    """
    Фикстура для предоставления базового URL API.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    return base_url


@pytest.fixture(scope="function")
def api_client():
    """
    Фикстура для создания клиента API .
    """
    api_client = requests.Session()
    yield api_client
    api_client.close()  # Закрываем сессию после завершения тестов
