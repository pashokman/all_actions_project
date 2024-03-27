from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from utilities.logger import Logger


logger_instance = Logger(log_name='Base page')
BASEPAGE = logger_instance.get_logger()


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def open_page(self, url):
        self.driver.get(url)


    def get_element(self, locator_name, locator_value):
        try:
            element = None
            if locator_name.endswith("_XPATH"):
                element = self.driver.find_element(By.XPATH, locator_value)
            elif locator_name.endswith("_ID"):
                element = self.driver.find_element(By.ID, locator_value)
            elif locator_name.endswith("_NAME"):
                element = self.driver.find_element(By.NAME, locator_value)
            elif locator_name.endswith("_LINK_TEXT"):
                element = self.driver.find_element(By.LINK_TEXT, locator_value)
            elif locator_name.endswith("_CLASS"):
                element = self.driver.find_element(By.CLASS_NAME, locator_value)
            elif locator_name.endswith("_CSS"):
                element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
            
            return element
        except NoSuchElementException as e:
            print('Cant find element - ', e)
            BASEPAGE.warning(f'Cant find element - {e}')
        except Exception as e:
            print('Non handled exception - ', e)
            BASEPAGE.warning(f'Non handled exception - {e}')


    def get_elements_list(self, locator_name, locator_value):
        elements = None
        if locator_name.endswith("_XPATH"):
            elements = self.driver.find_elements(By.XPATH, locator_value)
        elif locator_name.endswith("_ID"):
            elements = self.driver.find_elements(By.ID, locator_value)
        elif locator_name.endswith("_NAME"):
            elements = self.driver.find_elements(By.NAME, locator_value)
        elif locator_name.endswith("_LINK_TEXT"):
            elements = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_CLASS"):
            elements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_CSS"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        
        return elements
    

    def type_into_element(self, locator_name, locator_value, text):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)


    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()


    def check_display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()
    

    def retrive_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text
    

    def enter_file_into_field(self, locator_name, locator_value, file_path):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(file_path)
