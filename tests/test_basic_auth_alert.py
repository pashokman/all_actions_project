import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.auth
class TestBasicAuth(BaseTest):
    def test_authentication_valid_credentials(self, driver, logs_for_tests):
        home_page = HomePage(driver)

        basic_auth_page = home_page.navigate_to_basic_auth_page('admin', 'admin')

        err_msg = 'Login with valid credentials failed'
        assert basic_auth_page.check_successful_login(), err_msg and logs_for_tests.warning(err_msg)

        expected_page_header = 'Basic Auth'
        expected_successful_login_msg = 'Congratulations! You must have the proper credentials.'

        header_err_msg = 'Header does not match'
        actuacl_header_text = basic_auth_page.get_page_header_text()
        assert actuacl_header_text == expected_page_header, header_err_msg and logs_for_tests.warning(header_err_msg)
        
        login_err_msg = 'Login message does not match'
        actuacl_login_msg_text = basic_auth_page.get_login_msg_text()
        assert actuacl_login_msg_text == expected_successful_login_msg, \
            login_err_msg and logs_for_tests.warning(login_err_msg)
