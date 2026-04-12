from app.pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self._username_input = "[data-test='username']"
        self._password_input = "[data-test='password']"
        self._login_button = "[data-test='login-button']"
        self._title = ".title"

    def load(self, url: str) -> None:
        self.open(url)

    def login(self, username: str, password: str) -> None:
        self.fill(self._username_input, username)
        self.fill(self._password_input, password)
        self.click(self._login_button)

    def get_title(self) -> str:
        self.wait_for(self._title)
        return self.get_text(self._title)
