import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.upload_download
class TestUploadDownload(BaseTest):
    def test_upload_file(self, driver, logs_for_tests):
        home_page = HomePage(driver)
        
        file_upload_page = home_page.navigate_to_file_upload_page()
        file_upload_page.upload_file()
        file_upload_successful_page = file_upload_page.send_file()

        header = file_upload_successful_page.get_page_header()
        file_name = file_upload_successful_page.get_uploaded_file_name()

        expected_header = 'File Uploaded!'
        err_header_msg = f'Actual message - {header}. Expected message - {expected_header}'
        assert header == expected_header, err_header_msg and logs_for_tests.warning(err_header_msg)

        expected_file_name = file_upload_page.get_file_name()
        err_file_name_msg = f'Actual file name - {file_name}. Expected file name - {expected_file_name}'
        assert file_name == expected_file_name, err_file_name_msg and logs_for_tests.warning(err_file_name_msg)


