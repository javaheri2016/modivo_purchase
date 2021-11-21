import sys
sys.path.append(sys.path[0] + "/...")
from selenium import webdriver
from src.TestBase.test_setup import WebDriverSetup
from tests.test_data import TestData
from src.PageObject.Pages.home_page import Home
from src.PageObject.Pages.shop_page import *
import unittest
from time import sleep


class ModivoShopPage(WebDriverSetup):
    # Opens Modivo page and goes to the product page
    def test_cart_checkout(self):
        driver = self.driver
        self.driver.get(TestData.url_modivo)
        self.driver.set_page_load_timeout(30)

        home = Home(driver)
        shop = Shop(driver)
        home.cookies.click()
        shop.woman_section.click()
        shop.clothes_section.click()
        ad = Ad(driver)
        ad.close_ad.click()
        clothes = Clothes(driver)
        clothes.shirts_section.click()
        clothes.size.click()
        filter_woman = FilterWoman(driver)
        filter_woman.size_woman.click()
        filter_woman_up = FilterWomanUp(driver)
        filter_woman_up.size_woman_up.click()
        filter_size = FilterSize(driver)
        filter_size.checkbox_size.click()
        clothes.offer.click()
        filter_offer = FilterOffer(driver)
        filter_offer.checkbox_new.click()
        filter_offer.choose_filter.click()
        sleep(10)
        results = Results(driver)
        results.chosen_item.click()


if __name__ == '__main__':
    unittest.main()
