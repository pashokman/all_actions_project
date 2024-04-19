from selenium.webdriver import ActionChains

from pages.base_page import BasePage

from utilities.logger import Logger
from utilities.work_with_files.wait_file_for_download import wait_for_download
from utilities.work_with_files.delete_file import delete_file
from utilities.work_with_files.is_file_path_exist import is_file_path_exist


logger_instance = Logger(log_name='JQuery UI Menu page')
JQUERY_MENU = logger_instance.get_logger()


class JQueryUIMenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    ENABLED_ITEM_LINK_TEXT = 'Enabled'
    DOWNLOADS_ITEM_LINK_TEXT = 'Downloads'
    PDF_ITEM_LINK_TEXT = 'PDF'


    def download_menu_pdf_file(self, file_name):
        enabled = self.get_element('ENABLED_ITEM_LINK_TEXT', self.ENABLED_ITEM_LINK_TEXT)
        JQUERY_MENU.debug('Got Enabled menu item.')

        actions = ActionChains(self.driver)
        actions.move_to_element(enabled).perform()
        JQUERY_MENU.debug('Moved to Enabled menu item.')

        downloads = self.get_element('DOWNLOADS_ITEM_LINK_TEXT', self.DOWNLOADS_ITEM_LINK_TEXT)
        JQUERY_MENU.debug('Got Downloads menu item.')
        
        actions.move_to_element(downloads).perform()
        JQUERY_MENU.debug('Moved to Downloads menu item.')

        pdf = self.get_element('PDF_ITEM_LINK_TEXT', self.PDF_ITEM_LINK_TEXT)
        JQUERY_MENU.debug('Got PDF menu item.')
        
        actions.move_to_element(pdf).click().perform()
        JQUERY_MENU.debug('Moved to PDF menu item and click it.')

        self.download_file(file_name)


    def download_file(self, file_name):
        if wait_for_download(self.DOWNLOAD_FOLDER_PATH, file_name, timeout=5):
            JQUERY_MENU.debug(f"Download '{file_name}' file completed successfully.")
        else:
            JQUERY_MENU.error(f"Download '{file_name}' file failed or time out.")


    def file_on_a_disk(self, file_name):
        if is_file_path_exist('files', 'download', file_name):
            JQUERY_MENU.debug(f'File "{file_name}" exist on a disk.')
            return True
        else:
            JQUERY_MENU.debug(f'File "{file_name}" doesn\'t exist on a disk.')
            return False


    def delete_downloaded_file(self, file_name):
        if delete_file('files', 'download', file_name):
            JQUERY_MENU.debug(f'File "{file_name}" deleted.')
        else:
            JQUERY_MENU.error(f'File "{file_name}" deletion failed!')
