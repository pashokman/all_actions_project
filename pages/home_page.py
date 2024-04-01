"""
https://the-internet.herokuapp.com/
"""

from pages.base_page import BasePage
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.file_upload_page import FileUploadPage
from pages.file_download_page import FileDownloadPage


from utilities.logger import Logger


logger_instance = Logger(log_name='Home page')
HOME_PAGE = logger_instance.get_logger()


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    ADD_REMOVE_ELEMENTS_PAGE_LINK_TEXT = 'Add/Remove Elements'
    FILE_UPLOAD_PAGE_LINK_TEXT = 'File Upload'
    FILE_DOWNLOAD_PAGE_LINK_TEXT = 'File Download'


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
