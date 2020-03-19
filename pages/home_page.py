import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.basepage import Page


class HomePage(Page):
    URL = '/'

    USER_DROPDOWN = (By.CSS_SELECTOR, ".ta-headerDropDownUser .dropdown-username")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.url = self.url + self.URL

    @allure.step("Wait for Home page opened")
    def wait_for_page_loaded(self):
        super().wait_for_page_loaded()
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(self.USER_DROPDOWN))
        self.logger.info('Home page is opened')
