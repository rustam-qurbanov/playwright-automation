from playwright.sync_api import Page

from app.pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._title = page.locator(".title")
        self._inventory_list = page.locator(".inventory_list")
        self._inventory_items = page.locator(".inventory_item")

    def get_title(self) -> str:
        self.wait_for(self._title)
        return self.get_text(self._title)

    def get_item_count(self) -> int:
        return self._inventory_items.count()

    def is_loaded(self) -> bool:
        return self.is_visible(self._inventory_list)

    def add_first_item_to_cart(self) -> None:
        add_btn = self.page.locator("button:has-text('Add to cart')").first
        self.click(add_btn)
