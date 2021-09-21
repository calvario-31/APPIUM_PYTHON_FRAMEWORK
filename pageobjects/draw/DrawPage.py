import allure
from appium.webdriver.common.mobileby import MobileBy

import utilities.log_manager as log
from pageobjects.Page import Page


class DrawPage(Page):
    _clearButton = (MobileBy.ACCESSIBILITY_ID, "test-CLEAR")
    _saveButton = (MobileBy.ACCESSIBILITY_ID, "test-SAVE")
    _okButton = (MobileBy.ID, "android:id/button1")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Save and clear canvas")
    def save_and_clear_canvas(self):
        self._wait_to_load()
        log.info("Clicking on save button")
        self._find(self._saveButton).click()
        log.info("Clicking on ok button")
        self._wait_visibility(self._okButton).click()
        log.info("Clicking on clear button")
        self._wait_visibility(self._clearButton).click()

    @allure.step("Drawing rectangle")
    def draw_rectangle(self):
        self._wait_to_load()
        log.info("Drawing rectangle")
        self._vertical_swipe(0.4, 0.8, 0.3)
        self._horizontal_swipe(0.3, 0.8, 0.8)
        self._vertical_swipe(0.8, 0.4, 0.8)
        self._horizontal_swipe(0.8, 0.3, 0.4)

    @allure.step("Drawing square")
    def draw_square(self):
        self._wait_to_load()
        log.info("Drawing square")
        self._vertical_swipe(0.5, 0.8, 0.3)
        self._horizontal_swipe(0.3, 0.8, 0.8)
        self._vertical_swipe(0.8, 0.5, 0.8)
        self._horizontal_swipe(0.8, 0.3, 0.5)

    @allure.step("Drawing medical cross")
    def draw_medical_cross(self):
        self._wait_to_load()
        log.info("Drawing medical cross")
        self._vertical_swipe(0.4, 0.7, 0.5)
        self._horizontal_swipe(0.2, 0.8, 0.55)

    @allure.step("Drawing x letter")
    def draw_x_letter(self):
        self._wait_to_load()
        log.info("Drawing x letter")
        self._general_swipe(0.25, 0.5, 0.75, 0.7)
        self._general_swipe(0.75, 0.5, 0.25, 0.7)

    @allure.step("Drawing t letter")
    def draw_t_letter(self):
        self._wait_to_load()
        log.info("Drawing t letter")
        self._vertical_swipe(0.5, 0.8, 0.5)
        self._horizontal_swipe(0.2, 0.8, 0.5)

    def _wait_to_load(self):
        self._wait_visibility(self._clearButton)
