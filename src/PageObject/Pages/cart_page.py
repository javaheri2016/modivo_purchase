import sys
sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from src.PageObject.locators import Locators


class Cart(object):
    def __init__(self, driver):
        self.driver = driver
        self.regular_price = driver.find_element(By.XPATH, Locators.cart_regular_price)
        self.discounted_price = driver.find_element(By.XPATH, Locators.cart_discounted_price)
        self.final_price = driver.find_element(By.XPATH, Locators.cart_final_price)
        self.total_price = driver.find_element(By.XPATH, Locators.total_cart_value)
        self.go_to_checkout = driver.find_element(By.XPATH, Locators.go_to_checkout_btn)


class Account(object):
    def __init__(self, driver):
        self.driver = driver
        self.guest = driver.find_element(By.XPATH, Locators.guest_checkout_btn)


class Checkout(object):
    def __init__(self, driver):
        self.driver = driver
        self.item_value = driver.find_element(By.XPATH, Locators.item_value)
        self.total_value = driver.find_element(By.XPATH, Locators.total_value)
        self.email = driver.find_element(By.XPATH, Locators.form_email_input)
        self.phone = driver.find_element(By.XPATH, Locators.form_phone_input)
        self.first_name = driver.find_element(By.XPATH, Locators.form_first_name_input)
        self.last_name = driver.find_element(By.XPATH, Locators.form_last_name_input)
        self.street = driver.find_element(By.XPATH, Locators.form_street_input)
        self.street_no = driver.find_element(By.XPATH, Locators.form_street_no_input)
        self.zip = driver.find_element(By.XPATH, Locators.form_zip_code_input)
        self.city = driver.find_element(By.XPATH, Locators.form_city_input)
        self.dhl = driver.find_element(By.XPATH, Locators.shipping_dhl)
        self.payu = driver.find_element(By.XPATH, Locators.payment_payu)
        self.zip = driver.find_element(By.XPATH, Locators.form_zip_code_input)
        self.all_checkboxes = driver.find_element(By.XPATH, Locators.check_all_checkboxes)
        self.pay_btn = driver.find_element(By.XPATH, Locators.order_and_pay_btn)


class Payment1(object):
    def __init__(self, driver):
        self.driver = driver
        self.by_card = driver.find_element(By.XPATH, Locators.pay_by_card_btn)


class Payment2(object):
    def __init__(self, driver):
        self.driver = driver
        self.insert_details = driver.find_element(By.XPATH, Locators.insert_card_details_btn)


class Payment3(object):
    def __init__(self, driver):
        self.driver = driver
        self.card_number = driver.find_element(By.XPATH, Locators.card_number_input)
        self.card_exp = driver.find_element(By.XPATH, Locators.card_exp_date_input)
        self.card_cvv = driver.find_element(By.XPATH, Locators.card_cvv_input)
        self.pay = driver.find_element(By.XPATH, Locators.pay_btn)


class PaymentFailed(object):
    def __init__(self, driver):
        self.driver = driver
        self.auth_failed = driver.find_element(By.XPATH, Locators.authorization_failed)
        self.close = driver.find_element(By.XPATH, Locators.close_and_return_btn)


class PaymentError(object):
    def __init__(self, driver):
        self.driver = driver
        self.order = driver.find_element(By.XPATH, Locators.repayment_btn)
        self.repayment = driver.find_element(By.XPATH, Locators.order_status)