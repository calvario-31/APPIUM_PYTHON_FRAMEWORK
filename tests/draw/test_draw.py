import allure
import pytest
from appium.webdriver.webdriver import WebDriver

from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.draw.DrawPage import DrawPage
from pageobjects.menu.TopMenuPage import TopMenuPage
from utilities.datareader.test_reader import get_standard_credentials


class TestDraw:
    driver: WebDriver
    login_page: LoginPage
    draw_page: DrawPage
    top_menu_page: TopMenuPage

    @allure.title("Draw rectangle test")
    @allure.description("Playing drawing a rectangle")
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase("2E5cHwYs", "Test case")
    @pytest.mark.regression
    def test_draw_rectangle(self, credentials):
        self.login_page.login(credentials["username"], credentials["password"])
        self.top_menu_page.go_to_draw_page()
        self.draw_page.draw_rectangle()
        self.draw_page.save_and_clear_canvas()

    @allure.title("Draw square test")
    @allure.description("Playing drawing a square")
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase("2E5cHwYs", "Test case")
    @pytest.mark.regression
    def test_draw_square(self, credentials):
        self.login_page.login(credentials["username"], credentials["password"])
        self.top_menu_page.go_to_draw_page()
        self.draw_page.draw_square()
        self.draw_page.save_and_clear_canvas()

    @allure.title("Draw medial cross test")
    @allure.description("Playing drawing a medial cross")
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase("2E5cHwYs", "Test case")
    @pytest.mark.regression
    def test_draw_medical_cross(self, credentials):
        self.login_page.login(credentials["username"], credentials["password"])
        self.top_menu_page.go_to_draw_page()
        self.draw_page.draw_medical_cross()
        self.draw_page.save_and_clear_canvas()

    @allure.title("Draw a t letter test")
    @allure.description("Playing drawing a t letter")
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase("2E5cHwYs", "Test case")
    @pytest.mark.regression
    def test_draw_t_letter(self, credentials):
        self.login_page.login(credentials["username"], credentials["password"])
        self.top_menu_page.go_to_draw_page()
        self.draw_page.draw_t_letter()
        self.draw_page.save_and_clear_canvas()

    @allure.title("Draw x letter test")
    @allure.description("Playing drawing a x letter")
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase("2E5cHwYs", "Test case")
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_draw_x_letter(self, credentials):
        self.login_page.login(credentials["username"], credentials["password"])
        self.top_menu_page.go_to_draw_page()
        self.draw_page.draw_x_letter()
        self.draw_page.save_and_clear_canvas()

    def init_pages(self):
        self.login_page = LoginPage(self.driver)
        self.top_menu_page = TopMenuPage(self.driver)
        self.draw_page = DrawPage(self.driver)

    @pytest.fixture(params=get_standard_credentials())
    def credentials(self, request):
        return request.param
