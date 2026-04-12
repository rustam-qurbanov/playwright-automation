import pytest
from typing import Dict


@pytest.fixture
def auth_data() -> Dict[str, str]:
    """Provides standard user authentication data."""
    import os

    return {
        "username": os.getenv("TEST_USER", "standard_user"),
        "password": os.getenv("TEST_PASSWORD", "secret_sauce"),
    }
