import pytest


@pytest.fixture
def api_client():
    """Provides an API client instance (stub)."""

    class APIClientStub:
        pass

    return APIClientStub()
