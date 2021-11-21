import sys
sys.path.append(sys.path[0] + "/...")
from selenium import webdriver
from src.TestBase.test_setup import WebDriverSetup
from tests.test_data import TestData
from tests.TestScripts.test_product_page import ModivoProductPage
from src.PageObject.Pages.home_page import Home
from src.PageObject.Pages.shop_page import *
from src.PageObject.Pages.cart_page import *
import unittest
from time import sleep


class ModivoCartPage(WebDriverSetup):
    # Adds product to cart and go to checkout
    def test_cart_checkout(self):
        driver = self.driver
        ModivoProductPage.test_add_item_to_cart(self)
        cart = Cart(driver)
        check_final_price = cart.final_price.text
        cart.go_to_checkout.click()
        account = Account(driver)
        account.guest.click()
        checkout = Checkout(driver)
        item_price = checkout.item_value.text
        total_cart_price = checkout.total_value.text
        self.assertEqual(check_final_price, item_price, total_cart_price)
        checkout.email.send_keys(TestData.email)
        checkout.phone.send_keys(TestData.phone_number)
        checkout.first_name.send_keys(TestData.name)
        checkout.last_name.send_keys(TestData.last_name)
        checkout.street.send_keys(TestData.street)
        checkout.street_no.send_keys(TestData.street_number)
        checkout.zip.send_keys(TestData.zip_code)
        checkout.city.send_keys(TestData.city)
        checkout.dhl.click()
        sleep(5)
        checkout.payu.click()
        sleep(5)
        checkout.all_checkboxes.click()
        checkout.pay_btn.click()
        payment_step1 = Payment1(driver)
        payment_step1.by_card.click()
        payment_step2 = Payment2(driver)
        payment_step2.insert_details.click()
        payment_step3 = Payment3(driver)
        sleep(10)
        payment_step3.card_number.send_keys(TestData.card_number)
        payment_step3.card_exp.send_keys(TestData.card_exp_date)
        payment_step3.card_cvv.send_keys(TestData.card_cvv)
        payment_step3.pay.click()
        payment_fail = PaymentFailed(driver)
        payment_fail.close.click()
        payment_error = PaymentError(driver)
        payment_error.order.is_displayed()
        payment_error.repayment.is_enabled()


if __name__ == '__main__':
    unittest.main()