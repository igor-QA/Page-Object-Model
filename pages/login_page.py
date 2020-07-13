from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Url isn\'t have "login" in self'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not find'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not find'

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)

        input_email.send_keys(email)
        input_password.send_keys(password)
        input_confirm_password.send_keys(password)

        submit_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        submit_btn.click()