import sys
sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from src.PageObject.locators import Locators


class Product(object):
    def __init__(self, driver):
        self.driver = driver
        self.regular_price = driver.find_element(By.XPATH, Locators.regular_price)
        self.discounted_price = driver.find_element(By.XPATH, Locators.discounted_price)
        self.final_price = driver.find_element(By.XPATH, Locators.final_price)
        self.add_to_cart = driver.find_element(By.XPATH, Locators.add_to_cart_btn)


class Size(object):
    def __init__(self, driver):
        self.driver = driver
        self.choose_size = driver.find_element(By.XPATH, Locators.choose_size)


class PopUp(object):
    def __init__(self, driver):
        self.driver = driver
        self.regular_price = driver.find_element(By.XPATH, Locators.popup_regular_price)
        self.discounted_price = driver.find_element(By.XPATH, Locators.popup_discounted_price)
        self.final_price = driver.find_element(By.XPATH, Locators.popup_final_price)
        self.show_cart = driver.find_element(By.XPATH, Locators.show_cart)