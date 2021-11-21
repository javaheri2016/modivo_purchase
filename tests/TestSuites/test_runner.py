import sys
sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())
import unittest
from unittest import TestLoader, TestSuite, TextTestRunner
from tests.TestScripts.test_home_page import ModivoHomePage
from tests.TestScripts.test_shop_page import ModivoShopPage
from tests.TestScripts.test_product_page import ModivoProductPage
from tests.TestScripts.test_cart_page import ModivoCartPage


if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(ModivoHomePage),
        test_loader.loadTestsFromTestCase(ModivoShopPage),
        test_loader.loadTestsFromTestCase(ModivoProductPage),
        test_loader.loadTestsFromTestCase(ModivoCartPage),
    ))
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)