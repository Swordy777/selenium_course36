import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link = "https://google.com"

def test_addtobasket_exists(browser):
    browser.get(link)
    try:
        add_to_basket = browser.find_element(By.CSS_SELECTOR,"button.btn-add-to-basket")
    except NoSuchElementException:
        add_to_basket = None
        print("NoSuchElementException: Couldn't find the 'Add to basket' button")
    time.sleep(2)
    assert add_to_basket is not None, "Test failed, check the exception message for details"
