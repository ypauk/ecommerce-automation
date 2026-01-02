import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

USE_WEBDRIVER_MANAGER = os.getenv("USE_WEBDRIVER_MANAGER", "0") == "1"
HEADLESS = os.getenv("HEADLESS", "1") == "1"
IS_WINDOWS = platform.system() == "Windows"

if USE_WEBDRIVER_MANAGER:
    from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-extensions")

    if HEADLESS:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    if USE_WEBDRIVER_MANAGER:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    return driver