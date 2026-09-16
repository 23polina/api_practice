import pytest

from api.client import ApiClient


@pytest.fixture()
def api_client():
    return ApiClient(
        base_url="https://himaxym.com/api/v1/data",
    )