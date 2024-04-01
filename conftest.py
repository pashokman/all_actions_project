from selenium import webdriver

from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.edge.options import Options as EOptions

import allure
from allure_commons.types import AttachmentType

import pytest

from utilities.read_configurations import read_configuration
from utilities.logger import Logger
from utilities.work_with_files.get_specific_path import get_full_path


# screenshoot fixtures  -----------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------------------------------



# main driver fixture --------------------------------------------------------------------------------------------------
FILES_FOLDER_PATH = get_full_path('files', 'download')
browsers = read_configuration("browsers", "browser_list").split(',')

@pytest.fixture(params=browsers)
def driver(request):
    global driver
    if request.param == "chrome":
        chrome_options = COptions()
        chrome_options.add_experimental_option('prefs', {'download.default_directory': FILES_FOLDER_PATH})
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FOptions()
        firefox_options.set_preference('browser.download.folderList', 2)
        firefox_options.set_preference('browser.download.manager.showWhenStarting', False)
        firefox_options.set_preference('browser.download.dir', FILES_FOLDER_PATH)
        firefox_options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
        driver = webdriver.Firefox(options=firefox_options)
    elif request.param == "edge":
        edge_options = EOptions()
        edge_options.add_experimental_option('prefs', {'download.default_directory': FILES_FOLDER_PATH})
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    
    driver.maximize_window()

    logger = Logger(log_name='BROWSER').get_logger()
    logger.info(driver.name)

    app_url = read_configuration("basic info", "url")
    driver.get(app_url)
    
    yield driver
    
    driver.quit()
# ----------------------------------------------------------------------------------------------------------------------


# fixture for adding logs row about start and end of every test --------------------------------------------------------
@pytest.fixture()
def logs_for_tests(request):
    test_name = request.function.__name__
    logger = Logger(log_name=test_name).get_logger()
    logger.debug('Test start.')

    yield logger

    logger.debug('Test completed.')
#  ---------------------------------------------------------------------------------------------------------------------