import allure
from appium.webdriver.common.mobileby import MobileBy

import utilities.log_manager as log
from pageobjects.Page import Page


class TopMenuPage(Page):
    _burger_menu = (MobileBy.ACCESSIBILITY_ID, "test-Menu")
    _draw_option = (MobileBy.ACCESSIBILITY_ID, "test-DRAWING")
    _logout_option = (MobileBy.ACCESSIBILITY_ID, "test-LOGOUT")
    _checkout_button = (MobileBy.ACCESSIBILITY_ID, "test-Cart")
    _items_count = (MobileBy.ANDROID_UIAUTOMATOR,
                    "description(\"test-Cart\").childSelector(className(\"android.widget.TextView\"))")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Going to the draw page")
    def go_to_draw_page(self):
        self._wait_to_load()
        log.info("Clicking on the burger menu")
        self._find(self._burger_menu).click()
        log.info("Clicking on the draw option")
        self._wait_visibility(self._draw_option).click()

    @allure.step("Going to the checkout page")
    def go_to_checkout(self):
        log.info("Going to the checkout")
        self._find(self._checkout_button).click()

    @allure.step("Getting items count")
    def get_items_count(self):
        self._wait_to_load()
        log.info("Getting the items count from the ui")
        return int(self._find(self._items_count).text)

    @allure.step("Logging out")
    def log_out(self):
        self._wait_to_load()
        log.info("Clicking on the burger menu")
        self._find(self._burger_menu).click()
        log.info("Clicking on the logout option")
        self._wait_visibility(self._logout_option).click()

    def _wait_to_load(self):
        self._wait_visibility(self._burger_menu)
