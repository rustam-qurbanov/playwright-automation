import pytest
from config.settings import BASE_URL


@pytest.mark.ui
def test_add_multiple_items_to_cart(
    auth_flow, header, inventory_page, cart_page, auth_data
):
    """Test ID: [CART-02]"""
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])

    # Act
    # Each time we click index 0, the button text changes to "Remove",
    # so the next "Add to cart" button becomes index 0.
    inventory_page.add_item_by_index(0)
    inventory_page.add_item_by_index(0)
    inventory_page.add_item_by_index(0)

    # Assert badge
    assert header.is_cart_badge_visible()
    assert header.get_cart_count() == "3"

    # Assert cart items list
    header.open_cart()
    assert cart_page.get_items_in_cart() == 3


@pytest.mark.ui
def test_remove_item_from_inventory(auth_flow, header, inventory_page, auth_data):
    """Test ID: [CART-03]"""
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])
    inventory_page.add_item_by_index(0)
    assert header.get_cart_count() == "1"

    # Act
    inventory_page.remove_item_by_index(0)

    # Assert
    assert not header.is_cart_badge_visible()


@pytest.mark.ui
def test_remove_item_from_cart(auth_flow, header, inventory_page, cart_page, auth_data):
    """Test ID: [CART-04]"""
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])
    inventory_page.add_item_by_index(0)
    header.open_cart()
    assert cart_page.get_items_in_cart() == 1

    # Act
    cart_page.remove_item_by_index(0)

    # Assert
    assert cart_page.get_items_in_cart() == 0
    assert not header.is_cart_badge_visible()


@pytest.mark.ui
def test_cart_state_persistence_after_reload(
    auth_flow, header, inventory_page, cart_page, auth_data
):
    """Test ID: [CART-05]"""
    # Arrange
    auth_flow.login_as(BASE_URL, auth_data["username"], auth_data["password"])
    inventory_page.add_item_by_index(0)
    inventory_page.add_item_by_index(0)

    # Act: Reload the page
    inventory_page.page.reload()

    # Assert
    assert header.is_cart_badge_visible()
    assert header.get_cart_count() == "2"

    header.open_cart()
    assert cart_page.get_items_in_cart() == 2
