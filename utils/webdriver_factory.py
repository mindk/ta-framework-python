import logging
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.config import get_config
from utils.webdriver_event_listener import WebDriverListener


class WebDriverFactory:

    def __init__(self):
        self.remote = get_config('remote')
        self.host = get_config('host')
        self.port = get_config('port')
        self.browser = get_config('browser')
        self.base_url = get_config('base_url')

    def get_browser(self):
        if self.remote and self.host is None:
            self.host = "127.0.0.1"
        if self.remote and self.port is None:
            self.port = "4444"

        if self.browser == "chrome":
            desired_capabilities = DesiredCapabilities.CHROME.copy()
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--ignore-certificate-errors")
            if self.remote:
                try:
                    driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                                              options=options,
                                              command_executor="http://" + self.host + ":" + self.port + "/wd/hub")
                except Exception:
                    logging.exception("WebDriver Host is not available")
                    raise ConnectionError("WebDriver Host is not available")
            else:
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        elif self.browser == "firefox":
            desired_capabilities = DesiredCapabilities.FIREFOX.copy()
            options = webdriver.FirefoxOptions()
            if self.remote:
                try:
                    driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                                              options=options,
                                              command_executor="http://" + self.host + ":" + self.port + "/wd/hub")
                except Exception:
                    logging.exception("WebDriver Host is not available")
                    raise ConnectionError("WebDriver Host is not available")
            else:
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        else:
            raise Exception("Provide valid browser name")

        driver.maximize_window()

        try:
            urlopen(self.base_url)
        except Exception:
            driver.quit()
            raise Exception("Target host is not available")

        w_driver = EventFiringWebDriver(driver, WebDriverListener())
        w_driver.get(self.base_url)

        return w_driver
