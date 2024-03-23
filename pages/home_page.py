"""
https://the-internet.herokuapp.com/
"""

from pages.base_page import BasePage
from pages.add_remove_elements_page import AddRemoveElementsPage

from utilities.Logger import Logger


logger_instance = Logger(log_name='Home page')
HOME_PAGE = logger_instance.get_logger()


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    PAGE_ADDRESS = 'https://the-internet.herokuapp.com/'
    ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT = 'Add/Remove Elements'


    def navigate_to_add_remove_elements_page(self):
        self.element_click('ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT', self.ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT)
        HOME_PAGE.debug('Navigation to add/remove page successful.')
        return AddRemoveElementsPage(self.driver)


