"""
https://the-internet.herokuapp.com/
"""

import requests

from pages.base_page import BasePage
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.file_upload_page import FileUploadPage
from pages.file_download_page import FileDownloadPage
from pages.basic_auth_page import BasicAuthPage
from pages.broken_image_page import BrokenImagePage
from pages.checkboxes_page import CheckboxesPage
from pages.context_menu_page import ContextMenuPage
from pages.geolocation_page import GeolocationPage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.hovers_page import HoversPage

from utilities.logger import Logger


logger_instance = Logger(log_name='Home page')
HOME_PAGE = logger_instance.get_logger()


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT = 'Add/Remove Elements'
    FILE_UPLOAD_PAGE_LINK_TEXT = 'File Upload'
    FILE_DOWNLOAD_PAGE_LINK_TEXT = 'File Download'
    BROKEN_IMAGE_LINK_TEXT = 'Broken Images'
    CHECKBOXES_LINK_TEXT = 'Checkboxes'
    CONTEXT_MENU_LINK_TEXT = 'Context Menu'
    GEOLOCATION_LINK_TEXT = 'Geolocation'
    HORIZONTAL_SLIDER_LINK_TEXT = 'Horizontal Slider'
    HOVERS_LINK_TEXT = 'Hovers'
    LINKS_XPATH = '//a'


    def navigate_to_add_remove_elements_page(self):
        self.element_click('ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT', self.ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT)
        HOME_PAGE.debug('Navigation to add/remove page.')
        return AddRemoveElementsPage(self.driver)


    def navigate_to_file_upload_page(self):
        self.element_click('FILE_UPLOAD_PAGE_LINK_TEXT', self.FILE_UPLOAD_PAGE_LINK_TEXT)
        HOME_PAGE.debug('Navigation to file upload page.')
        return FileUploadPage(self.driver)


    def navigate_to_file_download_page(self):
        self.element_click('FILE_DOWNLOAD_PAGE_LINK_TEXT', self.FILE_DOWNLOAD_PAGE_LINK_TEXT)
        HOME_PAGE.debug('Navigation to file download page.')
        return FileDownloadPage(self.driver)


    def navigate_to_basic_auth_page(self, login, pwd):
        self.driver.get(f'https://{login}:{pwd}@the-internet.herokuapp.com/basic_auth')
        HOME_PAGE.debug('Navigation to basic auth page.')
        return BasicAuthPage(self.driver)


    def navigate_to_broken_images_page(self):
        self.element_click('BROKEN_IMAGE_LINK_TEXT', self.BROKEN_IMAGE_LINK_TEXT)
        HOME_PAGE.debug('Navigation to broken images page.')
        return BrokenImagePage(self.driver)


    def find_broken_links_href(self):
        links_list = self.get_elements_list('LINKS_XPATH', self.LINKS_XPATH)
        result = []

        for i in range(len(links_list)):
            href = links_list[i].get_attribute('href')
            response = requests.get(href)
            
            if response.status_code >= 404:
                result.append(href)

        HOME_PAGE.debug(f'Broken links href: {result}')
        return result


    def navigate_to_checkboxes_page(self):
        self.element_click('CHECKBOXES_LINK_TEXT', self.CHECKBOXES_LINK_TEXT)
        HOME_PAGE.debug('Navigation to checkboxes page.')
        return CheckboxesPage(self.driver)


    def navigate_to_context_menu_page(self):
        self.element_click('CONTEXT_MENU_LINK_TEXT', self.CONTEXT_MENU_LINK_TEXT)
        HOME_PAGE.debug('Navigation to context menu page.')
        return ContextMenuPage(self.driver)


    def navigate_to_geolocation_page(self):
        self.element_click('GEOLOCATION_LINK_TEXT', self.GEOLOCATION_LINK_TEXT)
        HOME_PAGE.debug('Navigation to geolocation page.')
        return GeolocationPage(self.driver)


    def navigate_to_horizontal_slider_page(self):
        self.element_click('HORIZONTAL_SLIDER_LINK_TEXT', self.HORIZONTAL_SLIDER_LINK_TEXT)
        HOME_PAGE.debug('Navigation to horizontal slider page.')
        return HorizontalSliderPage(self.driver)


    def navigate_to_hovers_page(self):
        self.element_click('HOVERS_LINK_TEXT', self.HOVERS_LINK_TEXT)
        HOME_PAGE.debug('Navigation to hovers page.')
        return HoversPage(self.driver)