import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    """
    Pytest fixture to initialize a Chrome WebDriver instance for UI tests.
    The browser runs in incognito mode with common settings disabled
    to prevent popups and password manager prompts from interfering with tests.
    """

    options = Options()

    # Incognito mode to isolate browser session
    options.add_argument("--incognito")

    # Disable password leak detection and save password popups
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-save-password-bubble")

    # Disable infobars, notifications, extensions, sync and first-run checks
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-sync")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    # Disable Chrome password manager
    options.add_experimental_option(
        "prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    # Initialize Chrome WebDriver using webdriver-manager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()

    yield driver  # Provide the fixture value to the test

    # Quit browser after test execution
    driver.quit()
