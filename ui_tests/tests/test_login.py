import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(browser):
    page = LoginPage(browser)
    page.open("https://www.saucedemo.com")
    page.login("standard_user", "secret_sauce")
    inventory = InventoryPage(browser)
    assert "inventory" in browser.current_url

def test_invalid_login(browser):
    page = LoginPage(browser)
    page.open("https://www.saucedemo.com")
    page.login("wrong_user", "wrong_pass")
    assert "Username and password do not match" in page.get_error()

def test_locked_user(browser):
    page = LoginPage(browser)
    page.open("https://www.saucedemo.com")
    page.login("locked_out_user", "secret_sauce")
    assert "locked out" in page.get_error()
