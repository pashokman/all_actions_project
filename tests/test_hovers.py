import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.hovers
class TestHovers(BaseTest):
    def test_click_on_hover_element(self, driver, logs_for_tests):
        home_page = HomePage(driver)

        hovers_page = home_page.navigate_to_hovers_page()
        user_number = 2
        print(hovers_page.driver.current_url)
        hover_result_page = hovers_page.veiw_n_user_profile(user_number)

        exp_url = f'https://the-internet.herokuapp.com/users/{user_number}'
        curr_url = hover_result_page.get_current_url(exp_url)
        err_msg = f'Expected URL - {exp_url}, current URL - {curr_url}'
        assert curr_url, err_msg and logs_for_tests.error(err_msg)