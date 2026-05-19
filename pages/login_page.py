from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.ID, "error-message")
    LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"

    def login(self, username, password):
        """Perform login action with given username and password"""
        self.find_element(self.USERNAME_INPUT).send_keys(username)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        """Get the error message text if login fails"""
        return self.find_element(self.ERROR_MESSAGE).text