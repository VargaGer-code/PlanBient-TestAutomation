import pytest
import utilities.custom_logger as cl
import logging
from base.webdriverfactory import WebDriverFactory

log = cl.customLogger(logging.DEBUG)


@pytest.fixture(scope="class")
def getWebdriver(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebdriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")