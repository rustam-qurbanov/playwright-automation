import pytest

pytest_plugins = ["fixtures.ui", "fixtures.data", "fixtures.api"]


@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    """Global setup across all tests"""
    pass
