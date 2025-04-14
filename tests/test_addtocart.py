import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.data_loader import load_json

test_data = load_json('product_data.json')

@pytest.fixture
def perform_login(setup, url, valid_user):
    page = setup
    login_page = LoginPage(page)
    login_page.open(url)
    login_page.open_login_modal()
    home_page = login_page.login(valid_user["username"], valid_user["password"])
    return home_page

def test_add_products(setup, perform_login):
    page = setup
    home_page = HomePage(page)

    for category in test_data["categories"]:
        category_page = home_page.open_category(category["name"])
        product_detail_page = category_page.select_product(category["product"])
        product_detail_page.add_product_to_cart_and_return_home()

    cart_page = CartPage(page)
    cart_page.open()

    cart_page.expect_item_count(len(test_data["categories"]))
    cart_page.remove_all_items()