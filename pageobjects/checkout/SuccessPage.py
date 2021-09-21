import allure
from appium.webdriver.common.mobileby import MobileBy

import utilities.log_manager as log
from pageobjects.Page import Page


class SuccessPage(Page):
    _body_success = (MobileBy.ACCESSIBILITY_ID, "test-CHECKOUT: COMPLETE!")
    _back_to_home_button = (MobileBy.ACCESSIBILITY_ID, "test-BACK HOME")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Verifying if the success page is displayed")
    def success_title_is_displayed(self):
        log.info("Verifying if the success page is displayed")
        return self._element_is_displayed(self._body_success)

    @allure.step("Clicking back to home")
    def return_to_home(self):
        log.info("Clicking back to home")
        return self._find(self._back_to_home_button).click()

    def _wait_to_load(self):
        pass
