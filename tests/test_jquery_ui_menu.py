import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.jquery_ui_menu
class TestJQueryUIMenu(BaseTest):
    def test_download_pdf_file(self, driver, logs_for_tests):
        home_page = HomePage(driver)

        jquery_menu_page = home_page.navigate_to_jquery_ui_menu_page()
        FILE_NAME = 'menu.pdf'
        jquery_menu_page.download_menu_pdf_file(FILE_NAME)

        err_msg = f'File - "{FILE_NAME}" download failed'
        assert jquery_menu_page.file_on_a_disk(FILE_NAME), err_msg and logs_for_tests.error(err_msg)

        # delete the file
        jquery_menu_page.delete_downloaded_file(FILE_NAME)
        del_err_msg = f'File - "{FILE_NAME}" deletion failed!'
        assert jquery_menu_page.file_on_a_disk(FILE_NAME) == False, del_err_msg and logs_for_tests.error(del_err_msg)