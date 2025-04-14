import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from utils.data_loader import load_json
from utils.dialog_utils import handle_dialog

test_data = load_json('login_data.json')
url = test_data["url"]

def perform_login(page, user):
	login_page = LoginPage(page)
	login_page.open(url)
	login_page.open_login_modal()
	login_page.login(user["username"], user["password"])
	return login_page


@pytest.mark.parametrize('user', test_data["users"])
def test_login(setup, user):
	page = setup
	login_page = perform_login(page, user)

	welcome_text = login_page.get_welcome_text()
	print(f"Message is, {welcome_text}")
	expect(login_page.page.locator(login_page.welcome_message_selector)).to_contain_text("Welcome")


@pytest.mark.parametrize('user', test_data["invalid_users"])
def test_invalid_login(setup, user):
	page = setup
	alert_text = handle_dialog(page, lambda: perform_login(page, user))
	assert "wrong" in alert_text.lower() or "fill out" in alert_text.lower()
