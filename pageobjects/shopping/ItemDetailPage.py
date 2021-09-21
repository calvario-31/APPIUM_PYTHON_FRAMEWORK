import allure
from appium.webdriver.common.mobileby import MobileBy

import utilities.log_manager as log
from pageobjects.Page import Page


class ItemDetailPage(Page):
    _back_to_products_button = (MobileBy.ACCESSIBILITY_ID, "test-BACK TO PRODUCTS")
    _add_to_cart_button = "test-ADD TO CART"
    _price_label = "test-Price"

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Add item: {1}")
    def add_to_cart(self, item_name):
        self._wait_to_load()
        log.info("Verifying item name is displayed")
        self._scroll_into_text(item_name)
        text = self._scroll_into_description(self._price_label).text
        price_text = float(text[1:])
        log.info("Clicking on add to cart")
        self._scroll_into_description(self._add_to_cart_button).click()
        log.info("Clicking on back to products")
        self._find(self._back_to_products_button).click()
        return price_text

    def _wait_to_load(self):
        self._wait_visibility(self._back_to_products_button)
