import pytest
from config.settings import BASE_URL


@pytest.mark.smoke
@pytest.mark.ui
def test_user_can_add_item_and_checkout_successfully(
    auth_flow, checkout_flow, header, inventory_page, auth_data
):
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
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])

    # Act
    inventory_page.add_first_item_to_cart()

    # Assert
    assert header.is_cart_badge_visible()
    assert header.get_cart_count() == "1"
