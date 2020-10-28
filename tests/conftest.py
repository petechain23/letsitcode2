import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.fixture()
def setUp():
    print("\nSetup before run every method")
    yield
    print("\nTearDown after run every method")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("\nSetup begin to run test case")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("diayti27@gmail.com", "abcabc")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("\nTearDown end when run all test case")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")