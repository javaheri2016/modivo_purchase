import sys
sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from src.PageObject.locators import Locators


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.cookies = driver.find_element(By.XPATH, Locators.accept_cookies_btn)

    def get_accept_cookies(self):
        return self.cookies
