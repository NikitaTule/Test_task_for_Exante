import requests


class BaseMetods:

    @staticmethod
    def send_get_request(url, endpoint):
        response = requests.get(f"{url}/{endpoint}")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def send_post_request(url, endpoint, data):
        response = requests.post(f"{url}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def send_put_request(url, endpoint, data):
        response = requests.put(f"{url}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def send_delete_request(url, endpoint):
        response = requests.delete(f"{url}/{endpoint}")
        response.raise_for_status()
        return response
