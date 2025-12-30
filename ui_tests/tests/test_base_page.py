from pages.base_page import BasePage

def test_open_site(browser):
    """
    Test to verify that the Saucedemo site opens successfully.

    Steps:
        1. Open the main page of Saucedemo.
        2. Verify that the current URL contains 'saucedemo'.
    """
    page = BasePage(browser)
    page.open("https://www.saucedemo.com")

    assert "saucedemo" in browser.current_url, "Saucedemo site did not open correctly"
