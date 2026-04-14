from playwright.sync_api import Page

from app.components.base_component import BaseComponent


class HeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self._cart_link = page.locator(".shopping_cart_link")
        self._cart_badge = page.locator(".shopping_cart_badge")
        self._burger_menu_btn = page.locator("#react-burger-menu-btn")

    def open_cart(self) -> None:
        self.click(self._cart_link)

    def open_menu(self) -> None:
        self.click(self._burger_menu_btn)

    def get_cart_count(self) -> str:
        return self.get_text(self._cart_badge)

    def is_cart_badge_visible(self) -> bool:
        return self.is_visible(self._cart_badge)
