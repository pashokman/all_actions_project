from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.hovers_result_page import HoversResultPage

from utilities.logger import Logger


logger_instance = Logger(log_name='Hovers page')
HOVERS = logger_instance.get_logger()


class HoversPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    USERS_IMAGES_XPATH = '//div[@class="figure"]//img'
    PROFILES_LINK_TEXT = 'View profile'


    def veiw_n_user_profile(self, user_number: int):
        users = self.get_elements_list('USERS_IMAGES_XPATH', self.USERS_IMAGES_XPATH)
        HOVERS.debug('Got users.')

        actions = ActionChains(self.driver)
        actions.move_to_element(users[user_number-1]).perform()

        profile = self.get_element('PROFILES_LINK_TEXT', self.PROFILES_LINK_TEXT)
        HOVERS.debug(f'Got user {user_number} profile.')
        
        actions.move_to_element(profile).click().perform()
        HOVERS.debug(f'Open users {user_number} profile.')

        return HoversResultPage(self.driver)
