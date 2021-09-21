import allure
import pytest
from appium.webdriver.webdriver import WebDriver

from pageobjects.checkout.InformationPage import InformationPage
from pageobjects.checkout.OverviewPage import OverviewPage
from pageobjects.checkout.SuccessPage import SuccessPage
from pageobjects.checkout.YourCartPage import YourCartPage
from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.menu.TopMenuPage import TopMenuPage
from pageobjects.shopping.ItemDetailPage import ItemDetailPage
from pageobjects.shopping.ShoppingPage import ShoppingPage
from utilities.datareader.test_reader import get_standard_credentials, get_shopping_list
from utilities.fakedatagen.user_info import get_random_user_info


class TestShopping:
    driver: WebDriver
    login_page: LoginPage
    top_menu_page: TopMenuPage
    shopping_page: ShoppingPage
    item_detail_page: ItemDetailPage
    your_cart_page: YourCartPage
    information_page: InformationPage
    overview_page: OverviewPage
    success_page: SuccessPage

    @pytest.mark.regression
    @pytest.mark.debug
    @allure.title("Test shopping")
    @allure.description("Verify the shopping e2e functionality")
    @allure.testcase("2E5cHwYs", "Test case")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shopping(self, credentials, shopping_list, user_data):
        self.login_page.login(credentials.get("username"), credentials.get("password"))

        total_sum = 0.0
        for item_to_buy in shopping_list:
            item_name = item_to_buy.get("name")
            item_price = item_to_buy.get("price")
            self.shopping_page.go_to_detail(item_name)
            price = self.item_detail_page.add_to_cart(item_name)
            assert item_price == price
            total_sum += price

        assert self.top_menu_page.get_items_count() == len(shopping_list)

        self.top_menu_page.go_to_checkout()
        self.your_cart_page.click_on_checkout()
        self.information_page.fill_form(user_data.get("firstname"), user_data.get("lastname"),
                                        user_data.get("zipcode"))

        assert self.overview_page.get_total_price() == total_sum
        self.overview_page.finish_checkout()

        assert self.success_page.success_title_is_displayed()
        self.success_page.return_to_home()

        assert self.shopping_page.shopping_page_is_displayed()

    def init_pages(self):
        self.login_page = LoginPage(self.driver)
        self.top_menu_page = TopMenuPage(self.driver)
        self.shopping_page = ShoppingPage(self.driver)
        self.item_detail_page = ItemDetailPage(self.driver)
        self.your_cart_page = YourCartPage(self.driver)
        self.information_page = InformationPage(self.driver)
        self.overview_page = OverviewPage(self.driver)
        self.success_page = SuccessPage(self.driver)

    @pytest.fixture(params=get_standard_credentials())
    def credentials(self, request):
        return request.param

    @pytest.fixture(params=get_shopping_list())
    def shopping_list(self, request):
        return request.param

    @pytest.fixture(params=get_random_user_info())
    def user_data(self, request):
        return request.param
