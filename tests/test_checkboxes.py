import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.checkboxes
class TestCheckboxes(BaseTest):
    def test_select_checkbox_and_get_its_status(self, driver, logs_for_tests):
        home_page = HomePage(driver)
        
        checkboxes_page = home_page.navigate_to_checkboxes_page()
        checkboxes_page.select_checkbox(0)
        checkboxes_page.deselect_checkbox(1)
        
        first_checkbox_status = checkboxes_page.get_checkbox_status(0)
        second_checkbox_status = checkboxes_page.get_checkbox_status(1)

        err_msg = 'First checkbox is not checked.'
        assert first_checkbox_status == True, err_msg and logs_for_tests.error(err_msg)
        
        err_msg = 'Second checkbox is not checked.'
        assert second_checkbox_status == False, err_msg and logs_for_tests.error(err_msg)

