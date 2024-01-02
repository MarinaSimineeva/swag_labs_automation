from playwright.sync_api import Page, expect
from pages.base import Base
from locators.auth_page_locators import AuthLocators


class AuthPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.auth_title = page.locator(AuthLocators.auth_title)
        self.username_input = page.locator(AuthLocators.username_input)
        self.password_input = page.locator(AuthLocators.password_input)
        self.login_btn = page.locator(AuthLocators.login_btn)
        self.error = page.locator(AuthLocators.error)

    def pass_auth(self, username_value=None, password_value=None):
        if username_value and len(username_value) > 0:
            self.username_input.fill(username_value)
        if password_value and len(username_value) > 0:
            self.password_input.fill(password_value)
        self.login_btn.click()

    def check_error_alert(self, exp_text):
        expect(self.error).to_be_visible(visible=True, timeout=12000)
        expect(self.error).to_have_text(exp_text)