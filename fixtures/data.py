import os

import pytest


@pytest.fixture(scope="session")
def auth_data() -> dict:
    return {
        "username": os.getenv("TEST_USER", "standard_user"),
        "password": os.getenv("TEST_PASSWORD", ""),
    }
