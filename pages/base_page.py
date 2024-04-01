from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


logger_instance = Logger(log_name='Base page')
BASEPAGE = logger_instance.get_logger()


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def open_page(self, url):
        self.driver.get(url)


    def get_element(self, locator_name, locator_value):
        wait = WebDriverWait(self.driver, 10)

        try:
            element = None
            if locator_name.endswith("_XPATH"):
                element = wait.until(EC.element_to_be_clickable((By.XPATH, locator_value)))
            elif locator_name.endswith("_ID"):
                element = wait.until(EC.element_to_be_clickable((By.ID, locator_value)))
            elif locator_name.endswith("_NAME"):
                element = wait.until(EC.element_to_be_clickable((By.NAME, locator_value)))
            elif locator_name.endswith("_LINK_TEXT"):
                element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locator_value)))
            elif locator_name.endswith("_CLASS"):
                element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator_value)))
            elif locator_name.endswith("_CSS"):
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_value)))
            
            return element
        except NoSuchElementException as e:
            print('Cant find element - ', e)
            BASEPAGE.warning(f'Cant find element - {e}')
        except Exception as e:
            print('Non handled exception - ', e)
            BASEPAGE.warning(f'Non handled exception - {e}')


    def get_elements_list(self, locator_name, locator_value):
        wait = WebDriverWait(self.driver, 10)
        elements = None
        
        if locator_name.endswith("_XPATH"):
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, locator_value)))
        elif locator_name.endswith("_ID"):
            elements = wait.until(EC.presence_of_all_elements_located((By.ID, locator_value)))
        elif locator_name.endswith("_NAME"):
            elements = wait.until(EC.presence_of_all_elements_located((By.NAME, locator_value)))
        elif locator_name.endswith("_LINK_TEXT"):
            elements = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, locator_value)))
        elif locator_name.endswith("_CLASS"):
            elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, locator_value)))
        elif locator_name.endswith("_CSS"):
            elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator_value)))
        
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

    
    def return_to_previous_page(self, count):
        for i in range(count):
            self.driver.back()