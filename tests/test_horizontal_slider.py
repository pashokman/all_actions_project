import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.horizontal_slider
class TestHorizontalSlider(BaseTest):
    def test_slide_to_the_right(self, driver, logs_for_tests):
        home_page = HomePage(driver)

        horizontal_slider_page = home_page.navigate_to_horizontal_slider_page()
        exp_value = 4
        horizontal_slider_page.move_slider_element(exp_value)
        curr_value = horizontal_slider_page.get_slider_value()

        err_msg = 'Value is not as expected! Right'
        assert exp_value == curr_value, err_msg and logs_for_tests.error(err_msg)



    def test_slide_to_the_left(self, driver, logs_for_tests):
        home_page = HomePage(driver)

        
        horizontal_slider_page = home_page.navigate_to_horizontal_slider_page()
        first_value = 4
        horizontal_slider_page.move_slider_element(first_value)
        second_value = 2
        horizontal_slider_page.move_slider_element(second_value)
        curr_value = horizontal_slider_page.get_slider_value()

        err_msg = 'Value is not as expected! Left'
        assert second_value == curr_value, err_msg and logs_for_tests.error(err_msg)
