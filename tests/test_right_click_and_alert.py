import time
import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.context_menu
class TestContextMenuAndAlert(BaseTest):
    def test_right_click_and_close_alert(self, driver, logs_for_tests):
        home_page = HomePage(driver)

        context_menu_page = home_page.navigate_to_context_menu_page()
        context_menu_page.open_context_menu()
        
        msg = context_menu_page.get_alert_message()
        exp_msg = 'You selected a context menu'
        err_msg = f'Curent alert msg - "{msg}", expected msg - "{exp_msg}".'
        assert msg == exp_msg, err_msg and logs_for_tests.error(err_msg)
        
        context_menu_page.accept_the_alert()