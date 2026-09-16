import pytest

from api.client import ApiClient
from config import API_BASE_URL, API_TOKEN


@pytest.fixture()
def api_client():
    return ApiClient(
        base_url=API_BASE_URL,
        api_token=API_TOKEN
    )