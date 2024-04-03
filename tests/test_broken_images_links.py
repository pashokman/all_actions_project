import pytest

from pages.home_page import HomePage

from tests.base_test import BaseTest


@pytest.mark.broken_images_links
class TestBrokenImagesLinks(BaseTest):
    def test_find_broken_images(self, driver, logs_for_tests):
        home_page = HomePage(driver)

        broken_images_page = home_page.navigate_to_broken_images_page()
        images = broken_images_page.get_images_list()
        src = broken_images_page.find_broken_images_src(images)
        expected_src = ['https://the-internet.herokuapp.com/asdf.jpg', 'https://the-internet.herokuapp.com/hjkl.jpg']

        err_msg = 'There are more broken images'
        assert src == expected_src, err_msg and logs_for_tests.error(err_msg)


    def test_find_broken_links(self, driver, logs_for_tests):
        home_page = HomePage(driver)

        links = home_page.find_broken_links_href()
        expected_links = []

        err_msg = 'There are more broken links'
        assert links == expected_links, err_msg and logs_for_tests.error(err_msg)