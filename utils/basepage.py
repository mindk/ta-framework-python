import logging

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.webdriver_factory import WebDriverFactory


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging
        self.url = WebDriverFactory().base_url

    @allure.step("Open page")
    def open(self):
        self.driver.get(self.url)
        self.logger.info('Page is opened')

    @allure.step("Wait for Page loaded")
    def wait_for_page_loaded(self):
        WebDriverWait(self.driver, 10).until(ec.url_matches(self.url))
        self.logger.info('Page is opened')

    def wait_for_dom(self):
        try:
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return document.readyState == "complete";'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return jQuery.active == 0'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return typeof jQuery != "undefined"'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script(
                'return angular.element(document).injector().get("$http").pendingRequests.length === 0'))
        except Exception as e:
            logging.exception(e)
            return False
