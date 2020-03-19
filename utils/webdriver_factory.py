from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.config import get_config


class WebDriverFactory:

    def __init__(self):
        self.remote = get_config('remote')
        self.host = get_config('host')
        self.port = get_config('port')
        self.browser = get_config('browser')
        self.base_url = get_config('base_url')

    def get_browser(self):
        # TODO refactor logic
        desired_capabilities = None
        options = None
        driver = None
        if self.remote:
            if self.browser == "chrome":
                desired_capabilities = DesiredCapabilities.CHROME.copy()
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized")
                options.add_argument("--ignore-certificate-errors")
            elif self.browser == "firefox":
                desired_capabilities = DesiredCapabilities.FIREFOX.copy()
                options = webdriver.FirefoxOptions()
            driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                                      options=options,
                                      command_executor="http://" + self.host + ":" + self.port + "/wd/hub")
        elif not self.remote:
            if self.browser == "firefox":
                options = webdriver.FirefoxOptions()
                options.add_argument("--start-maximized")
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            elif self.browser == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized")
                options.add_argument("--ignore-certificate-errors")
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        else:
            raise Exception("Provide valid browser name")
        driver.maximize_window()
        driver.get(self.base_url)
        return driver
