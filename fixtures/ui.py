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
