# Simple checkout scenario - Modivo

This a project for web automation of modivo.pl (production environment).
Due to this fact please don't oversure this script.

Technology stack: [Python](https://www.python.org/), [Selenium](https://www.selenium.dev/), 
[UnitTest](https://docs.python.org/3/library/unittest.html).

Page Object Model was used as design pattern.

### Directory structure

```
src
├── PageObject                                          # page objects and locators
├── TestBase                                            # framework settings, webdriver settings
tests
├── TestScripts                                         # folder contains of test scripts
├── TestSuites                                          # folder contains of test suites 
├── test_data.py                                        # test data, credentials
```

### Local environment setup

To use this project Python 3.10. is required.

MacOS and Linux
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

Windows
```bash
python3.10 -m venv venv
\path\to\env\Scripts\activate
example: C:\Users\Username\venv\Scripts\activate.bat
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

The convention for managing Python dependency is as follows:
- add the dependencies into requirements.in
- call ```pip-compile``` or ```python3.10 -m piptools compile``` to create requirements.txt
- commit both files to repository.

To run tests locally Selenium Webdriver is required. 
In this project Selenium Webdriver is managed automatically by 
[Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager).
Be sure that you have updated version of [Chrome Browser](https://www.google.com/chrome/) on your device.

### Run locally

Run tests in a main project folder:

```
python3 tests/TestSuites/test_runner.py
```

Test suite contains of:

- ModivoHomePage - tests main page, cookies and title
- ModivoShopPage - tests categories and filters
- ModivoProductPage - tests product page and adding to cart
- ModivoCartPage - tests purchase process from product page till payment error
