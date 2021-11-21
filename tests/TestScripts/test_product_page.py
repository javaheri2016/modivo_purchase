import sys
sys.path.append(sys.path[0] + "/...")
from selenium import webdriver
from src.TestBase.test_setup import WebDriverSetup
from tests.test_data import TestData
from src.PageObject.Pages.home_page import Home
from src.PageObject.Pages.product_page import *
import unittest
from time import sleep


class ModivoProductPage(WebDriverSetup):
    # Opens Modivo product page and adds it to cart
    def test_add_item_to_cart(self):
        driver = self.driver
        self.driver.get(TestData.url_product)
        self.driver.set_page_load_timeout(30)

        home = Home(driver)
        home.cookies.click()
        product = Product(driver)
        check_price_product = product.final_price.text
        product.add_to_cart.click()
        sleep(5)
        size = Size(driver)
        size.choose_size.click()
        popup = PopUp(driver)
        check_price_popup = popup.final_price.text
        self.assertEqual(check_price_popup, check_price_product)
        popup.show_cart.click()


if __name__ == '__main__':
    unittest.main()
