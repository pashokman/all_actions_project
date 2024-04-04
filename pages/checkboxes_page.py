from pages.base_page import BasePage

from utilities.logger import Logger


logger_instance = Logger(log_name='Checkboxes page')
CHECKBOXES = logger_instance.get_logger()


class CheckboxesPage(BasePage):
    def __init__(seld, driver):
        super().__init__(driver)

    CHECKBOX_XPATH = '//input'

    def get_checkbox_status(self, checkbox_index):
        elements = self.get_elements_list('CHECKBOX_XPATH', self.CHECKBOX_XPATH)
        status = elements[checkbox_index].is_selected()
        CHECKBOXES.debug(f'Got checkbox {checkbox_index} status.')
        return status    
    
    def select_checkbox(self, checkbox_index):
        if self.get_checkbox_status(checkbox_index) == False:
            elements = self.get_elements_list('CHECKBOX_XPATH', self.CHECKBOX_XPATH)
            elements[checkbox_index].click()
            CHECKBOXES.debug(f'Checkbox {checkbox_index} selected.')

    def deselect_checkbox(self, checkbox_index):
        if self.get_checkbox_status(checkbox_index) == True:
            elements = self.get_elements_list('CHECKBOX_XPATH', self.CHECKBOX_XPATH)
            elements[checkbox_index].click()
            CHECKBOXES.debug(f'Checkbox {checkbox_index} deselected.')