import pytest
from tests.BaseTest import BaseTest

from pages.home_page import HomePage


@pytest.mark.add_remove_elements
class TestAddRemoveElements(BaseTest):

    def test_add_elements_on_a_page(self, driver):
        home_page = HomePage(driver)
        
        add_remove_page = home_page.navigate_to_add_remove_elements_page()
        add_remove_page.add_n_elements(4)
        created_elements_count = add_remove_page.get_added_elements_count()

        assert created_elements_count == 4


    def test_remove_elements_from_a_page(self, driver):
        home_page = HomePage(driver)
        
        add_remove_page = home_page.navigate_to_add_remove_elements_page()
        add_remove_page.add_n_elements(8)
        created_elements_count = add_remove_page.get_added_elements_count()

        assert created_elements_count == 8

        add_remove_page.remove_n_elements(5)
        created_elements_count_after_removing = add_remove_page.get_added_elements_count()

        assert created_elements_count_after_removing == 2