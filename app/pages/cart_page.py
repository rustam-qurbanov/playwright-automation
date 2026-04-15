from playwright.sync_api import Page
from app.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._checkout_button = page.locator("[data-test='checkout']")
        self._cart_items = page.locator(".cart_item")

    def click_checkout(self) -> None:
        self.click(self._checkout_button)

    def get_items_in_cart(self) -> int:
        return self._cart_items.count()
