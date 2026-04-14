from playwright.sync_api import Locator, Page


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: Locator) -> None:
        locator.click()

    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    def wait_for(self, locator: Locator, state: str = "visible") -> None:
        locator.wait_for(state=state)
