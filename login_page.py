from .pages.base_page import BasePage
from .pages.locators import MainPageLocators
from .pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.browser.current_url=='http://selenium1py.pythonanywhere.com/ru/accounts/login/', 'vse ok'

    def should_be_login_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.login_field), "Login field is not presented"
        assert self.is_element_present(*LoginPageLocators.login_passqord_field), "Login password is not presented"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.registration_email_field), "Login field is not presented"
        assert self.is_element_present(*LoginPageLocators.registration_password1_field), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.registration_password2_field), "Login password is not presented"