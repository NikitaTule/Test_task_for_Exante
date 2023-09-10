import pytest
import requests


@pytest.fixture(scope="function")
def base_url():
    """
    Фикстура для предоставления базового URL API.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    return base_url

