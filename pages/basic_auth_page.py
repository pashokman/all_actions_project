from pages.base_page import BasePage

from utilities.logger import Logger


logger_instance = Logger(log_name='Basic Auth Page')
BASIC_AUTH = logger_instance.get_logger()


class BasicAuthPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)


    HEADER_XPATH = '//h3'
    SUCCESSFUL_LOGIN_MSG_XPATH = '//div[@class="example"]/p'
    
    
    def check_successful_login(self):
        header_status = self.check_display_status_of_element('HEADER_XPATH', self.HEADER_XPATH)
        msg_status = self.check_display_status_of_element('SUCCESSFUL_LOGIN_MSG_XPATH', self.SUCCESSFUL_LOGIN_MSG_XPATH)

        if header_status and msg_status:
            BASIC_AUTH.debug('Login completed')
            return True
        else:
            BASIC_AUTH.debug('Login failed')
            return False


    def get_page_header_text(self):
        header = self.retrive_element_text('HEADER_XPATH', self.HEADER_XPATH)
        BASIC_AUTH.debug('Got page header.')
        return header
    

    def get_login_msg_text(self):
        msg = self.retrive_element_text('SUCCESSFUL_LOGIN_MSG_XPATH', self.SUCCESSFUL_LOGIN_MSG_XPATH)
        BASIC_AUTH.debug('Got login msg.')
        return msg
