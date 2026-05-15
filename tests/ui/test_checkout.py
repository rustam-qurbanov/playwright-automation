import pytest
from config.settings import BASE_URL


@pytest.mark.smoke
@pytest.mark.ui
def test_user_can_add_item_and_checkout_successfully(
    auth_flow, checkout_flow, header, inventory_page, auth_data
):
    """Test ID: [E2E-01]"""
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])

    # Act
    inventory_page.add_first_item_to_cart()
    header.open_cart()
    complete_page = checkout_flow.complete_full_checkout("QA", "Engineer", "10001")

    # Assert
    assert complete_page.get_success_message() == "Thank you for your order!"


@pytest.mark.ui
def test_cart_badge_updates_when_item_added(
    auth_flow, header, inventory_page, auth_data
):
    """Test ID: [CART-01]"""
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])

    # Act
    inventory_page.add_first_item_to_cart()

    # Assert
    assert header.is_cart_badge_visible()
    assert header.get_cart_count() == "1"


@pytest.mark.ui
def test_checkout_validation_error_when_fields_empty(
    auth_flow, header, inventory_page, cart_page, checkout_info_page, auth_data
):
    """Test ID: [CHK-01]"""
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])
    inventory_page.add_first_item_to_cart()
    header.open_cart()
    cart_page.click_checkout()

    # Act
    # Click continue without filling the form
    checkout_info_page.click_continue()

    # Assert
    assert checkout_info_page.is_error_visible()
    assert "Error: First Name is required" in checkout_info_page.get_error_message()
