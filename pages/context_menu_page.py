from pages.base_page import BasePage

from utilities.logger import Logger

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

logger_instance = Logger(log_name = 'Context menu page')
CONTEXT_MENU = logger_instance.get_logger()


class ContextMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.alert = Alert(driver)
        self.actionChains = ActionChains(driver)

    MENU_AREA_ID = 'hot-spot'


    def open_context_menu(self):
        self.actionChains.context_click(self.get_element('MENU_AREA_ID', self.MENU_AREA_ID)).perform()
        CONTEXT_MENU.debug('Clicked on right mouse button.')

    def get_alert_message(self):
        alert_text = self.alert.text
        CONTEXT_MENU.debug('Got alert text.')
        return alert_text
    
    def accept_the_alert(self):
        self.alert.accept()
        CONTEXT_MENU.debug('Accepted alert.')
