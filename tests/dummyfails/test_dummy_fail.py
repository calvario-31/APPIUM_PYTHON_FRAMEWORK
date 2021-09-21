import allure
import pytest
from appium.webdriver.webdriver import WebDriver

from pageobjects.credentials.LoginPage import LoginPage
from utilities.datareader.test_reader import get_standard_credentials


class TestDummyFail:
    driver: WebDriver
    login_page: LoginPage

    @allure.title("Dummy fail")
    @allure.description("Test to see the screenshot")
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase("2E5cHwYs", "Test case")
    @pytest.mark.fail
    def test_dummy_fail(self, credentials):
        self.login_page.login(credentials["username"], credentials["password"])
        assert self.login_page.error_message_is_displayed()

    def init_pages(self):
        self.login_page = LoginPage(self.driver)

    @pytest.fixture(params=get_standard_credentials())
    def credentials(self, request):
        return request.param
