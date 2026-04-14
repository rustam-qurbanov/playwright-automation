import pytest

from config.settings import BASE_URL


@pytest.mark.smoke
@pytest.mark.ui
def test_successful_login(auth_flow, auth_data):
    inventory_page = auth_flow.login_as(
        BASE_URL, auth_data["username"], auth_data["password"]
    )

    assert inventory_page.get_title() == "Products"
    assert inventory_page.is_loaded()


@pytest.mark.smoke
@pytest.mark.ui
def test_invalid_login_shows_error(login_page):
    login_page.load(BASE_URL)
    login_page.login("invalid_user", "wrong_password")

    assert login_page.is_error_visible()
    assert "Username and password do not match" in login_page.get_error_message()
