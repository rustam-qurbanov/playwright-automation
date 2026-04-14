from playwright.sync_api import Page

from app.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._username_input = page.locator("[data-test='username']")
        self._password_input = page.locator("[data-test='password']")
        self._login_button = page.locator("[data-test='login-button']")
        self._error_message = page.locator("[data-test='error']")

    def load(self, url: str) -> None:
        self.open(url)

    def login(self, username: str, password: str) -> None:
        self.fill(self._username_input, username)
        self.fill(self._password_input, password)
        self.click(self._login_button)

    def get_error_message(self) -> str:
        self.wait_for(self._error_message)
        return self.get_text(self._error_message)

    def is_error_visible(self) -> bool:
        return self.is_visible(self._error_message)
