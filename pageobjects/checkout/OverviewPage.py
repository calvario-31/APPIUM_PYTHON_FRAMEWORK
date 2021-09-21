import allure
from appium.webdriver.common.mobileby import MobileBy

import utilities.log_manager as log
from pageobjects.Page import Page


class OverviewPage(Page):
    _finish_button = "test-FINISH"
    _total_price_label_text = "Item total:"
    _item_list = (MobileBy.ACCESSIBILITY_ID, "test-CHECKOUT: OVERVIEW")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting the total price")
    def get_total_price(self):
        self._wait_to_load()
        log.info("Getting total price from the ui")
        total_price_text = self._scroll_into_text_contains(self._total_price_label_text).text
        log.debug("Total price as text: " + str(total_price_text))

        log.info("Scrolling down to checkout button and click")
        self._scroll_into_description(self._finish_button).click()

        return float(total_price_text[13:])

    @allure.step("Finishing checkout")
    def finish_checkout(self):
        log.info("Finishing checkout")
        self._scroll_into_description(self._finish_button).click()

    def _wait_to_load(self):
        self._wait_visibility(self._item_list)
