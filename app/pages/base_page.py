from playwright.sync_api import Page, Locator
from typing import Union


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def click(self, selector: Union[str, Locator]) -> None:
        if isinstance(selector, str):
            self.page.locator(selector).click()
        else:
            selector.click()

    def fill(self, selector: Union[str, Locator], value: str) -> None:
        if isinstance(selector, str):
            self.page.locator(selector).fill(value)
        else:
            selector.fill(value)

    def wait_for(self, selector: Union[str, Locator], state: str = "visible") -> None:
        if isinstance(selector, str):
            self.page.locator(selector).wait_for(state=state)
        else:
            selector.wait_for(state=state)

    def get_text(self, selector: Union[str, Locator]) -> str:
        if isinstance(selector, str):
            return self.page.locator(selector).inner_text()
        return selector.inner_text()

    def is_visible(self, selector: Union[str, Locator]) -> bool:
        if isinstance(selector, str):
            return self.page.locator(selector).is_visible()
        return selector.is_visible()
