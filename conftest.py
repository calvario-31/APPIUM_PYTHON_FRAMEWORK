import os
import string
from os import path
from typing import Any, Callable, Optional

from _pytest.config import hookimpl
from _pytest.fixtures import SubRequest
from pytest import fixture

import utilities.log_manager as log_manager
from utilities.browserstack_scripts import *
from utilities.driver_manager import build_remote_driver, build_local_driver, take_screenshot

ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'
ALLUREDIR_OPTION = '--alluredir'

driver: WebDriver
device_name: string
os_version: string
run_on_server: bool
actual_test_name: string


@fixture(scope="function", autouse=True)
def manage_driver(request):
    global driver, actual_test_name, device_name
    actual_test_name = request.node.name.partition("[")[0]

    if run_on_server:
        driver = build_remote_driver(device_name, os_version)
        write_test_name(driver, actual_test_name)
    else:
        driver = build_local_driver(device_name)

    log_manager.start_test(actual_test_name)

    request.cls.driver = driver
    request.instance.init_pages()
    yield
    driver.quit()


@fixture(scope="session", autouse=True)
def manage_session(request):
    global run_on_server, os_version, device_name
    device_name = request.config.getoption("--device_name")
    os_version = request.config.getoption("--os_version")
    run_on_server = os.environ.get("JOB_NAME")
    log_manager.log = log_manager.get_logger()


def pytest_addoption(parser):
    parser.addoption("--device_name", action="store", default="mobile_emulator")
    parser.addoption("--os_version", action="store", default="11")


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    global driver, run_on_server, actual_test_name
    report = (yield).get_result()
    if report.when == "call":
        setattr(item, "report", report)
        log_manager.end_test(report.outcome.upper())
        if run_on_server:
            if report.outcome == "passed":
                write_test_status_passed(driver)
            elif report.outcome == "skipped":
                write_test_status_skipped(driver)
            elif report.outcome == "failed":
                write_test_status_failed(driver)


@fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.report:
        if request.node.report.failed:
            take_screenshot(driver)


@fixture(autouse=True)
def write_env_properties(add_allure_environment_property: Callable) -> None:
    global device_name, os_version
    add_allure_environment_property('Device', device_name)
    add_allure_environment_property('OS', 'Android')
    add_allure_environment_property('OS Version', os_version)


@fixture(scope='session', autouse=True)
def add_allure_environment_property(request: SubRequest) -> Optional[Callable]:

    environment_properties = dict()

    def maker(key: str, value: Any):
        environment_properties.update({key: value})

    yield maker

    alluredir = request.config.getoption(ALLUREDIR_OPTION)

    if not alluredir or not path.isdir(alluredir) or not environment_properties:
        return

    allure_env_path = path.join(alluredir, ALLURE_ENVIRONMENT_PROPERTIES_FILE)

    with open(allure_env_path, 'w') as _f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        _f.write(data)
