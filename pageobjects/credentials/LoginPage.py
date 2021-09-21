import allure
from appium.webdriver.common.mobileby import MobileBy

from pageobjects.Page import Page
import utilities.log_manager as log


class LoginPage(Page):
    _input_username = (MobileBy.ACCESSIBILITY_ID, "test-Username")
    _input_password = (MobileBy.ACCESSIBILITY_ID, "test-Password")
    _login_button = (MobileBy.ACCESSIBILITY_ID, "test-LOGIN")
    _error_message = (MobileBy.ACCESSIBILITY_ID, "test-Error message")
    _title = (MobileBy.CLASS_NAME, "android.widget.ImageView")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Logging with username: {username} and password: {password}")
    def login(self, username, password):
        self._wait_to_load()
        log.info("Filling username")
        self._find(self._input_username).send_keys(username)
        log.info("Filling password")
        self._find(self._input_password).send_keys(password)
        log.info("Clicking on login")
        self._find(self._login_button).click()

    @allure.step("Verifying the error message is displayed")
    def error_message_is_displayed(self):
        return self._element_is_displayed(self._error_message)

    def _wait_to_load(self):
        self._wait_visibility(self._title)
