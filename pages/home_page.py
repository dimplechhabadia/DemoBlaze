from base_page import BasePage
from category_page import CategoryPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.category_selector = "a"

    def open_category(self, category_name):
        category_locator = f"{self.category_selector}:has-text('{category_name}')"
        self.click(category_locator)

        category_page = CategoryPage(self.page)
        return category_page