from playwright.sync_api import Page
from app.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._complete_header = page.locator(".complete-header")

    def get_success_message(self) -> str:
        self.wait_for(self._complete_header)
        return self.get_text(self._complete_header)
