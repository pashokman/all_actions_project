from pages.base_page import BasePage

from utilities.logger import Logger

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger_instance = Logger(log_name='Hovers result page')
HOVERS_RES = logger_instance.get_logger()


class HoversResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_current_url(self, url):
        if WebDriverWait(self.driver, 5).until(EC.url_matches(url)):
            return True
        return False
        