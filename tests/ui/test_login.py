import pytest
from config.settings import BASE_URL


@pytest.mark.smoke
@pytest.mark.ui
def test_login(login_page, auth_data):
    """Simple UI test for logging in at saucedemo"""
    login_page.load(BASE_URL)
    login_page.login(auth_data["username"], auth_data["password"])

    assert login_page.get_title() == "Products"
