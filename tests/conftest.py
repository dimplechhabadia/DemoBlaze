import pytest
from playwright.sync_api import sync_playwright

from utils.data_loader import load_json

browsers_to_test = ["chromium"]

@pytest.fixture(params=browsers_to_test, scope="function" )
def setup(request):
    browser_name = request.param
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def test_data():
    return load_json("login_data.json")

@pytest.fixture(scope="session")
def url(test_data):
    return test_data["url"]

@pytest.fixture(scope="session")
def valid_user(test_data):
    return test_data["users"][0]