import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_valid_login(browser):
    """
    Test successful login with valid credentials.
    Verifies that user is redirected to inventory page.
    """
    login_page = LoginPage(browser)
    login_page.open("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    assert "inventory" in browser.current_url, "User was not redirected to inventory page after login"

@pytest.mark.smoke
def test_invalid_login(browser):
    """
    Test login with invalid credentials.
    Verifies that the correct error message is displayed.
    """
    login_page = LoginPage(browser)
    login_page.open("https://www.saucedemo.com")
    login_page.login("wrong_user", "wrong_pass")

    error_text = login_page.get_error()
    assert "Username and password do not match" in error_text, f"Unexpected error message: {error_text}"

@pytest.mark.smoke
def test_locked_user(browser):
    """
    Test login with a locked out user.
    Verifies that the correct 'locked out' error message is displayed.
    """
    login_page = LoginPage(browser)
    login_page.open("https://www.saucedemo.com")
    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error()
    assert "locked out" in error_text, f"Unexpected error message: {error_text}"
