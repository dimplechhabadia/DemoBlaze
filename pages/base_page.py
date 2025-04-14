from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def find_element(self, selector: str):
        return self.page.query_selector(selector)

    def click(self, selector: str):
        self.page.click(selector)

    def input_text(self, selector: str, text: str):
        self.page.fill(selector, text)

    def wait_for_selector(self, selector: str, state="visible", timeout=10000):
        self.page.locator(selector).wait_for(state=state, timeout=timeout)

    def get_text(self, selector: str):
        return self.page.locator(selector).text_content()