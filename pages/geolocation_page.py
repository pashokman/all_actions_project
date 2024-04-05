from pages.base_page import BasePage

from utilities.logger import Logger


logger_instance = Logger(log_name = 'Context menu page')
CONTEXT_MENU = logger_instance.get_logger()


class GeolocationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    WHERE_AM_I_BTN_XPATH = '//p[@id="demo"]/following-sibling::button'
    LATITUDE_XPATH = '//div[@id="lat-value"]'
    LONGITUDE_XPATH = '//div[@id="long-value"]'


    def click_where_am_i_button(self):
        self.element_click('WHERE_AM_I_BTN_XPATH', self.WHERE_AM_I_BTN_XPATH)

    def get_location(self):
        latitude = self.retrive_element_text('LATITUDE_XPATH', self.LATITUDE_XPATH)
        longitude = self.retrive_element_text('LONGITUDE_XPATH', self.LONGITUDE_XPATH)
        return [latitude, longitude]

    def location_as_expected(self, exp_location, curr_location):
        err_msg_latitude = f'Latitude is - {curr_location[0]}, but expected - {exp_location[0]}'
        err_msg_longitude = f'Longitude is - {curr_location[1]}, but expected - {exp_location[1]}'

        lat = str(exp_location[0]).startswith(str(curr_location[0])[0:4])
        lon = str(exp_location[1]).startswith(str(curr_location[1])[0:4])

        if lat:
            if lon:
                return True
            else:
                CONTEXT_MENU.error(err_msg_longitude)
                return False
        else:
            CONTEXT_MENU.error(err_msg_latitude)
            return False