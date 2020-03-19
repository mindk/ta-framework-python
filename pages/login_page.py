import logging

import allure
from selenium.webdriver.common.by import By

from utils.basepage import Page


class LogInPage(Page):
    URL = '/login'

    USERNAME_FIELD = (By.ID, "login-username-field")
    PASSWORD_FIELD = (By.ID, "login-password-field")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.taButtonLogin")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.url = self.url + self.URL

    @allure.step("Login as user")
    def login(self, user):
        self.open()
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.logger.info("Login as user")
