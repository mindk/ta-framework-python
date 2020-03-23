import logging

from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        try:
            WebDriverWait(driver, 1000, poll_frequency=0.5).until(
                lambda wdriver: driver.execute_script('return document.readyState == "complete";'))
            WebDriverWait(driver, 1000, poll_frequency=0.5).until(
                lambda wdriver: driver.execute_script('return jQuery.active == 0'))
            WebDriverWait(driver, 1000, poll_frequency=0.5).until(
                lambda wdriver: driver.execute_script('return typeof jQuery != "undefined"'))
            WebDriverWait(driver, 1000, poll_frequency=0.5).until(lambda wdriver: driver.execute_script(
                'return angular.element(document).injector().get("$http").pendingRequests.length === 0'))
        except Exception as e:
            logging.exception(e)
            return False
