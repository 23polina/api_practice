import requests


class ApiClient:

    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_token}"
        }

    def get_endpoint(self, endpoint: str, params: dict | None = None):
        return requests.get(f"{self.base_url}/{endpoint}",
                            headers=self.headers,
                            params=params,
                            timeout=30)