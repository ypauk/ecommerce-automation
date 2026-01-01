import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

USE_WEBDRIVER_MANAGER = os.getenv("USE_WEBDRIVER_MANAGER", "0") == "1"
HEADLESS = os.getenv("HEADLESS", "1") == "1"

if USE_WEBDRIVER_MANAGER:
    from webdriver_manager.chrome import ChromeDriverManager

def create_chrome_driver():
    options = Options()

    # Headless для Docker / CI
    if HEADLESS:
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
    else:
        # Локально с GUI — incognito и отключение лишних всплывающих окон
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

    # Инициализация драйвера
    if USE_WEBDRIVER_MANAGER:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    return driver
