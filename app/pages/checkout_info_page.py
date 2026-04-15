from playwright.sync_api import Page
from app.pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._first_name = page.locator("[data-test='firstName']")
        self._last_name = page.locator("[data-test='lastName']")
        self._zip_code = page.locator("[data-test='postalCode']")
        self._continue_button = page.locator("[data-test='continue']")

    def fill_shipping_info(self, first: str, last: str, zip_code: str) -> None:
        self.fill(self._first_name, first)
        self.fill(self._last_name, last)
        self.fill(self._zip_code, zip_code)

    def click_continue(self) -> None:
        self.click(self._continue_button)
