import sys
sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from src.PageObject.locators import Locators


class Shop(object):
    def __init__(self, driver):
        self.driver = driver
        self.woman_section = driver.find_element(By.XPATH, Locators.woman_section)
        self.clothes_section = driver.find_element(By.XPATH, Locators.clothes_section)


class Ad(object):
    def __init__(self, driver):
        self.driver = driver
        self.close_ad = driver.find_element(By.XPATH, Locators.close_black_friday_ad)


class Clothes(object):
    def __init__(self, driver):
        self.driver = driver
        self.shirts_section = driver.find_element(By.XPATH, Locators.shirts_section)
        self.offer = driver.find_element(By.XPATH, Locators.offer_filter)
        self.size = driver.find_element(By.XPATH, Locators.size_filter)


class FilterOffer(object):
    def __init__(self, driver):
        self.driver = driver
        self.checkbox_new = driver.find_element(By.XPATH, Locators.checkbox_new)
        self.choose_filter = driver.find_element(By.XPATH, Locators.filter_choose_btn)


class FilterWoman(object):
    def __init__(self, driver):
        self.driver = driver
        self.size_woman = driver.find_element(By.XPATH, Locators.size_filter_woman)


class FilterWomanUp(object):
    def __init__(self, driver):
        self.driver = driver
        self.size_woman_up = driver.find_element(By.XPATH, Locators.size_filter_woman_upper_parts)


class FilterSize(object):
    def __init__(self, driver):
        self.driver = driver
        self.checkbox_size = driver.find_element(By.XPATH, Locators.checkbox_size)
        self.choose_filter = driver.find_element(By.XPATH, Locators.filter_choose_btn)


class Results(object):
    def __init__(self, driver):
        self.driver = driver
        self.chosen_item = driver.find_element(By.XPATH, Locators.choose_random_item)
