from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage

from utilities.logger import Logger


logger_instance = Logger(log_name='Horizontal slider page')
HOR_SLIDER = logger_instance.get_logger()


class HorizontalSliderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    HOR_SLIDER_INTUP_XPATH = '//input'
    HOR_SLIDER_SPAN_XPATH = '//div[@class="sliderContainer"]/span'


    def move_slider_element(self, n):
        if self.driver.name == 'firefox':
            matching = {0.5: -70, 1: -60, 1.5: -40, 2: -10, 2.5: 0, 3: 10, 3.5: 29, 4: 50, 4.5: 70, 5: 80}
        else:
            matching = {0.5: -40, 1: -30, 1.5: -20, 2: -10, 2.5: 0, 3: 10, 3.5: 20, 4: 30, 4.5: 50, 5: 60}
        element = self.get_element('HOR_SLIDER_INTUP_XPATH', self.HOR_SLIDER_INTUP_XPATH)
        ActionChains(self.driver)\
            .drag_and_drop_by_offset(element, matching[n], 0)\
            .perform()
        HOR_SLIDER.debug(f'Slide to the value - {n}')


    def get_slider_value(self):
        value = float(self.retrive_element_text('HOR_SLIDER_SPAN_XPATH', self.HOR_SLIDER_SPAN_XPATH))
        HOR_SLIDER.debug(f'Got slider value - {value}')
        return value
