from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url,\
            'Substring "login" not in current browser url'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM),\
            'Login form not present on the page'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM),\
            'Registration form not present on the page'

    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        password_field = self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD)
        confirm_password = self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        login_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password.send_keys(password)
        reg_btn.click()
