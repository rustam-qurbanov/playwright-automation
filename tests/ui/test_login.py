import pytest

from config.settings import BASE_URL


@pytest.mark.smoke
@pytest.mark.ui
def test_successful_login(auth_flow, auth_data):
    """Test ID: [AUTH-01]"""
    inventory_page = auth_flow.login_as(
        BASE_URL, auth_data["username"], auth_data["password"]
    )

    assert inventory_page.get_title() == "Products"
    assert inventory_page.is_loaded()


@pytest.mark.smoke
@pytest.mark.ui
def test_invalid_login_shows_error(login_page):
    """Test ID: [AUTH-02]"""
    login_page.load(BASE_URL)
    login_page.login("invalid_user", "wrong_password")

    assert login_page.is_error_visible()
    assert "Username and password do not match" in login_page.get_error_message()


@pytest.mark.ui
def test_locked_out_user_shows_error(login_page, auth_data):
    """Test ID: [AUTH-03]"""
    login_page.load(BASE_URL)
    login_page.login("locked_out_user", auth_data["password"])

    assert login_page.is_error_visible()
    assert "Sorry, this user has been locked out." in login_page.get_error_message()


@pytest.mark.ui
def test_logout_flow(auth_flow, header, login_page, auth_data):
    """Test ID: [AUTH-04]"""
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])

    # Act
    header.open_menu()
    header.click_logout()

    # Assert
    assert login_page.is_loaded()


@pytest.mark.ui
def test_protected_routes(inventory_page, login_page):
    """Test ID: [AUTH-05]"""
    # Act: Try to access inventory directly without logging in
    inventory_page.load(BASE_URL)

    # Assert: Should be redirected to login page with an error
    assert login_page.is_loaded()
    assert login_page.is_error_visible()
    assert (
        "You can only access '/inventory.html' when you are logged in."
        in login_page.get_error_message()
    )
