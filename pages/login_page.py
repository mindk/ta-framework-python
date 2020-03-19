import logging

import allure
from selenium.webdriver.common.by import By

from utils.basepage import Page


class LogInPage(Page):
    URL = '/login'

    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "key")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input#btn-login")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.url = self.url + self.URL

    @allure.step("Login as user")
    def login(self, user):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(user.email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.logger.info("Login as user")
