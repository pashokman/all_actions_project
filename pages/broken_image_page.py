from pages.base_page import BasePage

from utilities.logger import Logger

import requests


logger_instance = Logger(log_name='Basic Auth Page')
BROKEN_IMAGE = logger_instance.get_logger()


class BrokenImagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    IMAGES_XPATH = '//img'


    def get_images_list(self):
        images = self.get_elements_list('IMAGES_XPATH', self.IMAGES_XPATH)
        BROKEN_IMAGE.debug('Found all images on the page')
        return images
    

    def find_broken_images_src(self, images_list):
        result = []
  
        for i in range(len(images_list)):
            src = images_list[i].get_attribute('src')
            response = requests.get(src)
            
            if response.status_code >= 404:
                result.append(src)

        BROKEN_IMAGE.debug(f'Broken images src: {result}')
        return result