import unittest
from selenium import webdriver
import urllib3
import time
from time import sleep
import warnings
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.set_script_timeout(40)

    def tearDown(self):
        print("Cleanup of test environment")
        self.driver.close()
        self.driver.quit()
