import allure
import pytest
from appium.webdriver.webdriver import WebDriver

from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.menu.TopMenuPage import TopMenuPage
from utilities.datareader.test_reader import get_standard_credentials


class TestLogout:
    driver: WebDriver
    login_page: LoginPage
    top_menu_page: TopMenuPage

    @allure.title("Logout test")
    @allure.description("Verifying error message when trying to log with a locked user")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("2E5cHwYs", "Test case")
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_logout(self, credentials):
        self.login_page.login(credentials["username"], credentials["password"])
        self.top_menu_page.log_out()
        assert self.login_page.login_page_is_displayed()

    def init_pages(self):
        self.login_page = LoginPage(self.driver)
        self.top_menu_page = TopMenuPage(self.driver)

    @pytest.fixture(params=get_standard_credentials())
    def credentials(self, request):
        return request.param
