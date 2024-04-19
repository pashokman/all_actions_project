import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.upload_download
class TestUploadDownload(BaseTest):
    def test_upload_file(self, driver, logs_for_tests):
        home_page = HomePage(driver)
        
        # upload the file
        file_upload_page = home_page.navigate_to_file_upload_page()
        file_upload_page.enter_file()
        file_upload_successful_page = file_upload_page.send_file()

        header = file_upload_successful_page.get_page_header()
        file_name = file_upload_successful_page.get_uploaded_file_name()

        # check if upload completed
        expected_header = 'File Uploaded!'
        err_header_msg = f'Actual message - {header}. Expected message - {expected_header}'
        assert header == expected_header, err_header_msg and logs_for_tests.error(err_header_msg)

        expected_file_name = file_upload_page.get_file_name()
        err_file_name_msg = f'Actual file name - {file_name}. Expected file name - {expected_file_name}'
        assert file_name == expected_file_name, err_file_name_msg and logs_for_tests.error(err_file_name_msg)


    def test_download_file(self, driver, logs_for_tests):
        home_page = HomePage(driver)
        
        # prepare a file to download
        file_upload_page = home_page.navigate_to_file_upload_page()
        file_upload_page.enter_file()
        file_upload_successful_page = file_upload_page.send_file()
        file_upload_successful_page.return_to_home_page()
        
        # download the file
        file_name = 'file_to_upload.txt'

        file_download_page = home_page.navigate_to_file_download_page()
        file_download_page.download_file(file_name)

        err_msg = f'File - "{file_name}" download failed'
        assert file_download_page.file_on_a_disk(file_name), err_msg and logs_for_tests.error(err_msg)

        # delete the file
        file_download_page.delete_downloaded_file(file_name)
        del_err_msg = f'File - "{file_name}" deletion failed!'
        assert file_download_page.file_on_a_disk(file_name) == False, del_err_msg and logs_for_tests.error(del_err_msg)

