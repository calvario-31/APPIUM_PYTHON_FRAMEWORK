import allure
from appium.webdriver.common.mobileby import MobileBy

import utilities.log_manager as log
from pageobjects.Page import Page


class InformationPage(Page):
    _firstname_input = (MobileBy.ACCESSIBILITY_ID, "test-First Name")
    _lastname_input = (MobileBy.ACCESSIBILITY_ID, "test-Last Name")
    _zipcode_input = (MobileBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    _continue_button = (MobileBy.ACCESSIBILITY_ID, "test-CONTINUE")
    _body_info = (MobileBy.ACCESSIBILITY_ID, "test-Checkout: Your Info")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Filling the form with firstname: {1}, lastname: {2} and zipcode: {3}")
    def fill_form(self, firstname, lastname, zipcode):
        self._wait_to_load()
        log.info("Filling firstname")
        self._find(self._firstname_input).send_keys(firstname)
        log.info("Filling lastname")
        self._find(self._lastname_input).send_keys(lastname)
        log.info("Filling zipcode")
        self._find(self._zipcode_input).send_keys(zipcode)
        log.info("Clicking on continue")
        self._find(self._continue_button).click()

    def _wait_to_load(self):
        self._wait_visibility(self._body_info)
