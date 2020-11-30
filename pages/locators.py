from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_field=(By.CSS_SELECTOR, "#id_login-username")
    login_passqord_field = (By.CSS_SELECTOR, "#id_login-password")
    registration_email_field = (By.CSS_SELECTOR, "#id_registration-email")
    registration_password1_field = (By.CSS_SELECTOR, "#id_registration-password21")
    registration_password2_field = (By.CSS_SELECTOR, "#id_registration-password2")
