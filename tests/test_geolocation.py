import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.geolocation
class TestGeolocation(BaseTest):
    def test_get_location(self, driver, logs_for_tests):
        home_page = HomePage(driver)
        
        geolocation_page = home_page.navigate_to_geolocation_page()
        geolocation_page.click_where_am_i_button()

        location = geolocation_page.get_location()
        # FOR FIREFOX SHOULD SET LOCATION IN DRIVER PREFERENCES (WITHOUT THEM IT DOES NOT WORK)
        exp_location = [48.699, 26.584]

        err_msg = 'Location is different'
        assert geolocation_page.location_as_expected(exp_location, location), err_msg and logs_for_tests.error(err_msg)
