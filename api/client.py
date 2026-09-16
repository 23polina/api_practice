import requests


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_endpoint(self, endpoint: str, params: dict | None = None):
        return requests.get(f"{self.base_url}/{endpoint}",
                            params=params,
                            timeout=30)