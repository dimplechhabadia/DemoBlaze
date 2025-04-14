from pages.base_page import BasePage
from utils.dialog_utils import handle_dialog


class ProductDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.add_to_cart_button = "a:has-text('Add to cart')"
        self.home_button = "a:has-text('Home')"

    def add_to_cart(self):
        self.click(self.add_to_cart_button)

    def add_product_to_cart_and_return_home(self):
        handle_dialog(self.page, self.add_to_cart)
        self.click(self.home_button)
