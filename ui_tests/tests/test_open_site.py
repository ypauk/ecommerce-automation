def test_open_saucedemo(browser):
    browser.get("https://www.saucedemo.com")
    assert "saucedemo" in browser.current_url
