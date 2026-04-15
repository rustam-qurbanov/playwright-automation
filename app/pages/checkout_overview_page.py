from playwright.sync_api import Page
from app.pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._finish_button = page.locator("[data-test='finish']")

    def click_finish(self) -> None:
        self.click(self._finish_button)
