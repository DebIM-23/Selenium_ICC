from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//span[normalize-space()='My Account']")
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Login']")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    ACCOUNT_HEADER = (By.XPATH, "//h2[normalize-space()='My Account']")
    WARNING_ALERT = (By.CSS_SELECTOR, "div.alert-danger")

    def navigate_to_login(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGIN_LINK)

    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_visible(self.ACCOUNT_HEADER)

    def get_warning_message(self):
        return self.get_text(self.WARNING_ALERT)