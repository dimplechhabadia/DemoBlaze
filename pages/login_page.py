from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_link = 'a#login2'
        self.login_modal = '#logInModal'
        self.username_input = 'input#loginusername'
        self.password_input = 'input#loginpassword'
        self.login_button = 'button:has-text("Log in")'
        self.welcome_message_selector = '#nameofuser'

    def open_login_modal(self):
        self.click(self.login_link)
        self.wait_for_selector(self.login_button)

    def login(self, username: str, password: str):
        self.input_text(self.username_input, username)
        self.input_text(self.password_input, password)
        self.click(self.login_button)
        self.page.wait_for_timeout(2000)

    def get_welcome_text(self):
        self.wait_for_selector(self.welcome_message_selector)
        return self.get_text(self.welcome_message_selector)

