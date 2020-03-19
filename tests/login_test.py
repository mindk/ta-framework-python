import allure
import pytest

from data.factory_user import UserFactory
from pages.home_page import HomePage
from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_login(self):
        login_page = LogInPage(self.driver)
        home_page = HomePage(self.driver)

        user = UserFactory(
            username="python_test",
            email="python_test@example.com",
            password="qwer1234"
        )

        with allure.step("Login as user"):
            login_page.open()
            login_page.wait_for_page_loaded()
            login_page.login(user)
        with allure.step("Check Home Page is opened"):
            home_page.wait_for_page_loaded()
            home_page.verify_user_name(user)
            home_page.screen_shot("Home Page is opened")
