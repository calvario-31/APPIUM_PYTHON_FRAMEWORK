import allure
import pytest
from appium.webdriver.webdriver import WebDriver

from pageobjects.credentials.LoginPage import LoginPage
from utilities.datareader.test_reader import get_locked_out_credentials


class TestLockedUser:
    driver: WebDriver
    login_page: LoginPage

    @allure.title("Locked user test")
    @allure.description("Verifying error message when trying to log with a locked user")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("2E5cHwYs", "Test case")
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_locked_user(self, locked_user_credentials):
        login_page = LoginPage(self.driver)
        login_page.login(locked_user_credentials["username"], locked_user_credentials["password"])
        assert login_page.error_message_is_displayed()

    def init_pages(self):
        self.login_page = LoginPage(self.driver)

    @pytest.fixture(params=get_locked_out_credentials())
    def locked_user_credentials(self, request):
        return request.param
