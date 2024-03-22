import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from utilities.ReadConfigurations import read_configuration


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


browsers = read_configuration("browsers", "browser_list").split(',')
@pytest.fixture(params=browsers)
def driver(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    
    driver.maximize_window()

    app_url = read_configuration("basic info", "url")
    driver.get(app_url)

    yield driver
    
    driver.quit()

