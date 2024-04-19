from pages.base_page import BasePage

from utilities.logger import Logger


logger_instance = Logger(log_name='JQuery UI Menu page')
JQUERY_MENU = logger_instance.get_logger()


class JSAlertsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    JS_ALERT_XPATH = '//button[@onclick="jsAlert()"]'
    JS_CONFIRM_XPATH = '//button[@onclick="jsConfirm()"]'
    JS_PROMPT_XPATH = '//button[@onclick="jsPrompt()"]'
    RESULT_XPATH = '//p[@id="result"]'


    def open_js_alert(self):
        self.element_click('JS_ALERT_XPATH', self.JS_ALERT_XPATH)


    def accept_alert(self):
        self.driver.switch_to.alert.accept()


    def open_js_confirm(self):
        self.element_click('JS_CONFIRM_XPATH', self.JS_CONFIRM_XPATH)

    
    def cancel_confirm(self):
        self.driver.switch_to.alert.dismiss()
    
    
    def open_js_prompt(self):
        self.element_click('JS_PROMPT_XPATH', self.JS_PROMPT_XPATH)


    def enter_text_into_a_prompt(self):
        self.driver.switch_to.alert.send_keys('Hello')
        self.accept_alert()

    
    def get_result_text(self):
        return self.retrive_element_text('RESULT_XPATH', self.RESULT_XPATH)