import pytest
from playwright.sync_api import Page


@pytest.fixture
def base_page(page: Page):
    """Provides an instance of BasePage."""
    from app.pages.base_page import BasePage

    return BasePage(page)


@pytest.fixture
def login_page(page: Page):
    """Provides an instance of LoginPage."""
    from app.pages.login_page import LoginPage

    return LoginPage(page)
