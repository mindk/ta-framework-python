import allure
import pytest

from data.factory_user import UserFactory
from data.user import User
from pages.home_page import HomePage
from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_login(self):
        login_page = LogInPage(self.driver)
        home_page = HomePage(self.driver)

        new_user = UserFactory()

        with allure.step('Login as Admin'):
            login_page.wait_for_page_loaded()
            login_page.login(User(username='', password=''))
            home_page.wait_for_page_loaded()
            assert login_page.url not in self.driver.current_url

