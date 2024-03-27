from pages.base_page import BasePage

from utilities.logger import Logger


logger_instance = Logger(log_name='Add/Remove Elements page')
ADD_REMOVE_ELEMENTS = logger_instance.get_logger()


class AddRemoveElementsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    ADD_ELEMENT_BUTTON_XPATH = '//button[@onclick="addElement()"]'
    ADDED_ELEMENT_CLASS = 'added-manually'


    def add_n_elements(self, n):
        elements_to_add = n
        while n > 0:
            self.element_click('ADD_ELEMENT_BUTTON_XPATH', self.ADD_ELEMENT_BUTTON_XPATH)
            n -= 1
        ADD_REMOVE_ELEMENTS.debug(f"{elements_to_add} elements added.")


    def get_added_elements_count(self):
        elements_count = len(self.get_elements_list('ADDED_ELEMENT_CLASS', self.ADDED_ELEMENT_CLASS))
        ADD_REMOVE_ELEMENTS.debug("Elements count received.")
        return elements_count
    

    def remove_n_elements(self, n):
        elements_to_remove = n
        elements_list = self.get_elements_list('ADDED_ELEMENT_CLASS', self.ADDED_ELEMENT_CLASS)
        while n > 0:
            elements_list[len(elements_list) - 1].click()
            n -= 1
        ADD_REMOVE_ELEMENTS.debug(f"{elements_to_remove} elements removed.")