import traceback
from abc import abstractmethod

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.gestures import Gestures


class Page:
    def __init__(self, driver):
        self._driver: WebDriver = driver
        self._gestures: Gestures = Gestures(self._driver)

    def _find(self, locator):
        return self._driver.find_element(*locator)

    def _wait_visibility(self, locator, time_out=5):
        wait: WebDriverWait = WebDriverWait(self._driver, time_out)
        return wait.until(expected_conditions.visibility_of_element_located(locator))

    def _element_is_displayed(self, locator, time_out=5):
        try:
            self._wait_visibility(locator, time_out)
            return True
        except TimeoutException:
            print(traceback.print_stack())
            return False

    def _scroll_into_description(self, description):
        return self._gestures.scroll_into_description(description)

    def _scroll_into_text(self, text):
        return self._gestures.scroll_into_text(text)

    def _scroll_into_text_contains(self, text):
        return self._gestures.scroll_into_text_contains(text)

    def _to_top(self):
        return self._gestures.scroll_to_top()

    def _general_swipe(self, x1, x2, y1, y2):
        return self._gestures.general_swipe_by_percentages(x1, x2, y1, y2)

    def _press_back(self):
        return self._gestures.press_back()

    @abstractmethod
    def _wait_to_load(self):
        pass
