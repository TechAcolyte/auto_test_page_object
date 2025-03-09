import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url doesn't contain substring"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Email field in Login form isn't presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Password field in Login form isn't presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOTTEN_PASSWORD), "Forgotten password link in Login form isn't presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Submit button in Login form isn't presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Email field in Register form isn't presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Password field in Register form isn't presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), "Confirm password field in Register form isn't presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Submit button in Register form isn't presented"

    def register_new_user(self, email, password):
        self.get_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.get_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        time.sleep(10)
        button = self.get_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()