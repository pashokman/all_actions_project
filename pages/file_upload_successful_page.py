from pages.base_page import BasePage

from utilities.logger import Logger


logger_instance = Logger(log_name='File upload successful page')
FILE_UPLOAD_SUCCESSFUL = logger_instance.get_logger()


class FileUploadSuccessfulPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    HEADER_XPATH = '//h3'
    UPLOADED_FILE_ID = 'uploaded-files'

    
    def get_page_header(self):
        header = self.retrive_element_text('HEADER_XPATH', self.HEADER_XPATH)
        FILE_UPLOAD_SUCCESSFUL.debug('Got page header.')
        return header

    
    def get_uploaded_file_name(self):
        file_name = self.retrive_element_text('UPLOADED_FILE_ID', self.UPLOADED_FILE_ID)
        FILE_UPLOAD_SUCCESSFUL.debug('Got file name.')
        return file_name