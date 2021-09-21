import allure
from appium.webdriver.common.mobileby import MobileBy

import utilities.log_manager as log
from pageobjects.Page import Page


class ShoppingPage(Page):
    _title = (MobileBy.ACCESSIBILITY_ID, "test-Cart drop zone")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Going to detail of item: {1}")
    def go_to_detail(self, item_name):
        self._wait_to_load()
        log.info("Clicking on the item name")
        self._scroll_into_text(item_name).click()

    @allure.step("Verifying shopping page is displayed")
    def shopping_page_is_displayed(self):
        log.info("Verifying shopping page is displayed")
        return self._element_is_displayed(self._title)

    def _wait_to_load(self):
        self._wait_visibility(self._title)
