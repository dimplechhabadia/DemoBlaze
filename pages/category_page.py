from pages.base_page import BasePage
from pages.product_detail_page import ProductDetailPage

class CategoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_selector = ".card-title"

    def select_product(self, product_name):
        product_locator = f"{self.product_selector}:has-text('{product_name}')"
        self.click(product_locator)

        return ProductDetailPage(self.page)

