import requests

base_url = "https://jsonplaceholder.typicode.com"


class BaseMetods:

    @staticmethod
    def send_get_request(endpoint):
        response = requests.get(f"{base_url}/{endpoint}")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def send_post_request(endpoint, data):
        response = requests.post(f"{base_url}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def send_put_request(endpoint, data):
        response = requests.put(f"{base_url}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def send_delete_request(endpoint):
        response = requests.delete(f"{base_url}/{endpoint}")
        response.raise_for_status()
        return response
