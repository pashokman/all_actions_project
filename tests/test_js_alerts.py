import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.js_alert
class TestJSAlerts(BaseTest):
    def test_accept_js_alert(self, driver, logs_for_tests):
        home_page = HomePage(driver)
        js_alerts_page = home_page.navigate_to_js_alerts_page()
        js_alerts_page.open_js_alert()
        js_alerts_page.accept_alert()
        
        actual_text = js_alerts_page.get_result_text()
        expeced_text = 'You successfully clicked an alert'
        err_msg = f'JS Alert error. Actual text: "{actual_text}" not equal expected text: {expeced_text}'
        assert actual_text == expeced_text, err_msg and logs_for_tests.error(err_msg)


    def test_cancel_js_confirm_alert(self, driver, logs_for_tests):
        home_page = HomePage(driver)
        js_alerts_page = home_page.navigate_to_js_alerts_page()
        js_alerts_page.open_js_confirm()
        js_alerts_page.cancel_confirm()
        
        actual_text = js_alerts_page.get_result_text()
        expeced_text = 'You clicked: Cancel'
        err_msg = f'JS Confirm error. Actual text: "{actual_text}" not equal expected text: {expeced_text}'
        assert actual_text == expeced_text, err_msg and logs_for_tests.error(err_msg)


    def test_enter_text_into_a_prompt(self, driver, logs_for_tests):
        home_page = HomePage(driver)
        js_alerts_page = home_page.navigate_to_js_alerts_page()
        js_alerts_page.open_js_prompt()
        js_alerts_page.enter_text_into_a_prompt()
        
        actual_text = js_alerts_page.get_result_text()
        expeced_text = 'You entered: Hello'
        err_msg = f'JS Prompt error. Actual text: "{actual_text}" not equal expected text: {expeced_text}'
        assert actual_text == expeced_text, err_msg and logs_for_tests.error(err_msg)