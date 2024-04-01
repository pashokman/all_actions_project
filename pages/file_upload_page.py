from pages.base_page import BasePage
from pages.file_upload_successful_page import FileUploadSuccessfulPage

from utilities.work_with_files.get_specific_path import get_full_path
from utilities.work_with_files.file_name import get_file_name_from_path
from utilities.logger import Logger


logger_instance = Logger(log_name='File upload page')
FILE_UPLOAD = logger_instance.get_logger()


class FileUploadPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    FILE_UPLOAD_INTUP_ID = 'file-upload'
    UPLOAD_BTN_ID = 'file-submit'
    FILE_UPLOAD_PATH = get_full_path('files', 'upload', 'file_to_upload.txt')


    def enter_file(self):
        self.enter_file_into_field('FILE_UPLOAD_INTUP_ID', self.FILE_UPLOAD_INTUP_ID, self.FILE_UPLOAD_PATH)
        FILE_UPLOAD.debug('File added.')


    def send_file(self):
        self.element_click('UPLOAD_BTN_ID', self.UPLOAD_BTN_ID)
        FILE_UPLOAD.debug('File send.')
        return FileUploadSuccessfulPage(self.driver)
    
    
    def get_file_name(self):
        return get_file_name_from_path(self.FILE_UPLOAD_PATH)