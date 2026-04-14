from app.pages.inventory_page import InventoryPage
from app.pages.login_page import LoginPage


class AuthFlow:
    def __init__(self, login_page: LoginPage, inventory_page: InventoryPage):
        self._login_page = login_page
        self._inventory_page = inventory_page

    def login_as(self, url: str, username: str, password: str) -> InventoryPage:
        self._login_page.load(url)
        self._login_page.login(username, password)
        return self._inventory_page
