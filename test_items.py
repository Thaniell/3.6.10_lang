from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def is_element_present(browser):
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        return True
    except:
        return False

def test_guest_should_see_add_to_bin(browser):
    browser.get(link)
    assert is_element_present(browser) == True, "No add to bin button on coders-at-work page"
