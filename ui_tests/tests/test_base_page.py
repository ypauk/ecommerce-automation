from pages.base_page import BasePage

def test_open_site(browser):
    page = BasePage(browser)
    page.open("https://www.saucedemo.com")
    assert "saucedemo" in browser.current_url
