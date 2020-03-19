import logging
import os
import time

import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils.config import get_config
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

    def screen_shot(self, result_message):
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        if len(file_name) >= 200:
            file_name = str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../" + get_config("screenshots_dir")
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name=file_name,
                          attachment_type=allure.attachment_type.PNG)
            logging.info("Screenshot saved to directory: " + destination_file)
        except Exception:
            raise Exception()

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
