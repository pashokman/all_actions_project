from pages.base_page import BasePage

from utilities.work_with_files.get_specific_path import get_full_path
from utilities.work_with_files.wait_file_for_download import wait_for_download
from utilities.logger import Logger
from utilities.work_with_files.is_file_path_exist import is_file_path_exist
from utilities.work_with_files.delete_file import delete_file


logger_instance = Logger(log_name='File download page')
FILE_DOWNLOAD = logger_instance.get_logger()


class FileDownloadPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    DOWNLOAD_FOLDER_PATH = get_full_path('files', 'download')


    def download_file(self, file_name):
        self.element_click('FILE_DOWNLOAD_LINK_TEXT', file_name)
        if wait_for_download(self.DOWNLOAD_FOLDER_PATH, file_name, timeout=5):
            FILE_DOWNLOAD.debug("Download completed successfully.")
        else:
            FILE_DOWNLOAD.error("Download failed or time out.")


    def file_on_a_disk(self, file_name):
        return is_file_path_exist('files', 'download', file_name)
    
    
    def delete_downloaded_file(self, file_name):
        if delete_file('files', 'download', file_name):
            FILE_DOWNLOAD.debug('File deleted.')
        else:
            FILE_DOWNLOAD.error('File deletion failed!')