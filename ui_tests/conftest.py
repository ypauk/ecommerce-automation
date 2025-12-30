import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-sync")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    options.add_experimental_option(
        "prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()
