import allure
from appium.webdriver.common.mobileby import MobileBy

import utilities.log_manager as log
from pageobjects.Page import Page


class YourCartPage(Page):
    _checkout_button = "test-CHECKOUT"
    _description_label = (MobileBy.ANDROID_UIAUTOMATOR, "text(\"DESCRIPTION\")")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Scrolling and clicking on checkout")
    def click_on_checkout(self):
        log.info("Scrolling and clicking on checkout")
        self._scroll_into_description(self._checkout_button).click()

    def _wait_to_load(self):
        self._wait_visibility(self._description_label)
