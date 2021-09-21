import os

import allure
from allure_commons.types import AttachmentType
from appium.webdriver import webdriver

import utilities.log_manager as log


def build_local_driver(emulator_name):
    log.info("Building local driver")
    desired_cap = {
        "autoGrantPermissions": True,
        "appWaitActivity": "com.swaglabsmobileapp.MainActivity",
        "automationName": "uiautomator2",
        "app": os.path.abspath('resources/apk/sauceLabs.apk'),
        "platformName": "android",
        "device": emulator_name
    }

    return webdriver.WebDriver('http://127.0.0.1:4723/wd/hub', desired_cap)


def build_remote_driver(device_name, os_version):
    log.info("Building remote driver")
    browserstack_local = os.environ["BROWSERSTACK_LOCAL"]
    browserstack_local_identifier = os.environ["BROWSERSTACK_LOCAL_IDENTIFIER"]
    build_name = os.environ["BROWSERSTACK_BUILD_NAME"]
    username = os.environ["BROWSERSTACK_USERNAME"]
    access_key = os.environ["BROWSERSTACK_ACCESS_KEY"]
    app = os.environ["BROWSERSTACK_APP_ID"]

    remote_url = "https://{}:{}@hub-cloud.browserstack.com/wd/hub".format(username, access_key)

    capabilities = {
        'app': app,
        'autoGrantPermissions': True,
        'browserName': 'Android',
        'deviceName': device_name,
        'automationName': 'uiautomator2',
        'appWaitActivity': 'com.swaglabsmobileapp.MainActivity',
        'os_version': os_version,
        'real_mobile': True,
        '"browserstack.appium_version': '1.21.0',
        'browserstack.local': browserstack_local,
        'browserstack.localIdentifier': browserstack_local_identifier,
        'build': build_name,
        'browserstack.debug': 'true',
        'browserstack.console': 'info',
        'browserstack.networkLogs': 'true'
    }

    driver = webdriver.WebDriver(remote_url, desired_capabilities=capabilities)

    return driver


def take_screenshot(driver):
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
