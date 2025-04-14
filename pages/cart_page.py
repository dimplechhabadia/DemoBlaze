from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_link = "a#cartur"
        self.cart_rows_selector = "tbody > tr"
        self.delete_button_selector = "a:has-text('Delete')"
        self.cart_table_selector = "tbody"

    def open(self):
        self.click(self.cart_link)  # or use text selector: self.page.click("a:has-text('Cart')")

    def get_cart_items(self):
        return self.page.locator(self.cart_rows_selector)

    def expect_item_count(self, expected_count):
        cart_items = self.get_cart_items()
        expect(cart_items).to_have_count(expected_count)

    def expect_item_in_cart(self, product_name):
        product_locator = self.page.locator(f"tbody >> text={product_name}")
        expect(product_locator).to_be_visible()

    def remove_all_items(self):
        delete_buttons = self.page.locator(self.delete_button_selector)
        while delete_buttons.count() > 0:
            delete_buttons.first.click()
            self.page.wait_for_timeout(500)
