from pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    ADD_ELEMENT_BUTTON_XPATH = '//button[@onclick="addElement()"]'
    ADDED_ELEMENT_CLASS = 'added-manually'


    def add_n_elements(self, n):
        while n > 0:
            self.element_click('ADD_ELEMENT_BUTTON_XPATH', self.ADD_ELEMENT_BUTTON_XPATH)
            n -= 1


    def get_added_elements_count(self):
        return len(self.get_elements_list('ADDED_ELEMENT_CLASS', self.ADDED_ELEMENT_CLASS))


    def remove_n_elements(self, n):
        elements_list = self.get_elements_list('ADDED_ELEMENT_CLASS', self.ADDED_ELEMENT_CLASS)
        while n > 0:
            elements_list[len(elements_list) - 1].click()
            n -= 1