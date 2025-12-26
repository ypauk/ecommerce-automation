import pytest
from utils.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client():
    """
    Provides a reusable API client instance for all test modules.

    Session scope is used to initialize the client once per test run.
    """
    return ApiClient()
