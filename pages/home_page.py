"""
https://the-internet.herokuapp.com/
"""

from pages.base_page import BasePage
from pages.add_remove_elements_page import AddRemoveElementsPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    PAGE_ADDRESS = 'https://the-internet.herokuapp.com/'
    ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT = 'Add/Remove Elements'


    def navigate_to_add_remove_elements_page(self):
        self.element_click('ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT', self.ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT)
        return AddRemoveElementsPage(self.driver)


