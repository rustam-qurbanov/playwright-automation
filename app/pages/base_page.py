from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def wait_for(self, locator: Locator, state: str = "visible") -> None:
        locator.wait_for(state=state)

    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    def get_url(self) -> str:
        return self.page.url
