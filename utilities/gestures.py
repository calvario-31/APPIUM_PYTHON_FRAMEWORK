from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class Gestures:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def tap_element(self, element):
        action = TouchAction(self.driver)
        action.tap(element).perform()

    def long_tap_element(self, element, seconds):
        actions = TouchAction(self.driver)
        actions.long_press(element, seconds).release().perform()

    def tap_by_coordinates(self, x, y):
        action = TouchAction(self.driver)
        action.tap(x=x, y=y).wait(1000).release().perform()

    def long_tap_by_coordinates(self, x, y, seconds):
        action = TouchAction(self.driver)
        action.long_press(x=x, y=y).wait(seconds * 1000).release().perform()

    def move_from_element_to_another(self, initial_element, final_element, seconds):
        actions = TouchAction(self.driver)
        actions.long_press(initial_element, seconds).move_to(final_element).release().perform()

    def general_swipe_by_percentages(self, first_x_percentage, first_y_percentage, second_x_percentage,
                                     second_y_percentage):
        size = self.driver.get_window_size()
        x1 = int(size["width"] * first_x_percentage)
        y1 = int(size["height"] * first_y_percentage)
        x2 = int(size["width"] * second_x_percentage)
        y2 = int(size["height"] * second_y_percentage)

        action = TouchAction(self.driver)
        action.press(x=x1, y=y1).wait(1000).move_to(x=x2, y=y2).release().perform()

    def vertical_swipe_by_percentages(self, start_percentage, end_percentage, anchor_percentage):
        size = self.driver.get_window_size()
        anchor = int(size["width"] * anchor_percentage)
        start_point = int(size["height"] * start_percentage)
        end_point = int(size["height"] * end_percentage)

        action = TouchAction(self.driver)
        action.press(x=anchor, y=start_point).wait(1000).move_to(x=anchor, y=end_point).release().perform()

    def horizontal_swipe_by_percentages(self, start_percentage, end_percentage, anchor_percentage):
        size = self.driver.get_window_size()
        anchor = int(size["height"] * anchor_percentage)
        start_point = int(size["width"] * start_percentage)
        end_point = int(size["width"] * end_percentage)

        action = TouchAction(self.driver)
        action.press(x=start_point, y=anchor).wait(1000).move_to(x=end_point, y=anchor).release().perform()

    def scroll_to_top(self):
        return self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)")

    def scroll_into_text(self, text):
        return self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector().scrollable(true).instance(0))" +
            ".scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))")

    def scroll_into_text_contains(self, text):
        return self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector().scrollable(true).instance(0))" +
            ".scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))")

    def scroll_into_description(self, description):
        return self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector().scrollable(true).instance(0))" +
            ".scrollIntoView(new UiSelector().description(\"" + description + "\").instance(0))")

    def press_back(self):
        self.driver.back()
