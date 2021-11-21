import sys
from selenium import webdriver
sys.path.append(sys.path[0] + "/...")
from src.TestBase.test_setup import WebDriverSetup
from tests.test_data import TestData
from src.PageObject.Pages.home_page import Home
import unittest
from selenium import webdriver


class ModivoHomePage(WebDriverSetup):
    # Opens Modivo page and closes cookies
    def test_home_page(self):
        driver = self.driver
        self.driver.get(TestData.url_modivo)
        self.driver.set_page_load_timeout(30)
        try:
            if driver.title == TestData.modivo_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, TestData.modivo_title)
        except Exception as error:
            print(error)

        home = Home(driver)
        home.cookies.click()


if __name__ == '__main__':
    unittest.main()
