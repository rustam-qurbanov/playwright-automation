import pytest
from playwright.sync_api import Page


@pytest.fixture
def login_page(page: Page):
    from app.pages.login_page import LoginPage

    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page):
    from app.pages.inventory_page import InventoryPage

    return InventoryPage(page)


@pytest.fixture
def auth_flow(page: Page):
    """Flow для авторизации."""
    # Ленивый импорт чтобы избежать циклических зависимостей
    from app.pages.inventory_page import InventoryPage
    from app.pages.login_page import LoginPage
    from flows.auth_flow import AuthFlow

    return AuthFlow(LoginPage(page), InventoryPage(page))


@pytest.fixture
def header(page: Page):
    from app.components.header import HeaderComponent

    return HeaderComponent(page)


@pytest.fixture
def cart_page(page: Page):
    from app.pages.cart_page import CartPage

    return CartPage(page)


@pytest.fixture
def checkout_info_page(page: Page):
    from app.pages.checkout_info_page import CheckoutInfoPage

    return CheckoutInfoPage(page)


@pytest.fixture
def checkout_overview_page(page: Page):
    from app.pages.checkout_overview_page import CheckoutOverviewPage

    return CheckoutOverviewPage(page)


@pytest.fixture
def checkout_complete_page(page: Page):
    from app.pages.checkout_complete_page import CheckoutCompletePage

    return CheckoutCompletePage(page)


@pytest.fixture
def checkout_flow(page: Page):
    from app.pages.cart_page import CartPage
    from app.pages.checkout_complete_page import CheckoutCompletePage
    from app.pages.checkout_info_page import CheckoutInfoPage
    from app.pages.checkout_overview_page import CheckoutOverviewPage
    from flows.checkout_flow import CheckoutFlow

    return CheckoutFlow(
        CartPage(page),
        CheckoutInfoPage(page),
        CheckoutOverviewPage(page),
        CheckoutCompletePage(page),
    )
