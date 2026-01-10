import pytest
from ui_tests.core.driver_factory import create_chrome_driver


@pytest.fixture
def browser():
    """
    Pytest fixture for UI tests.
    Creates a Chrome WebDriver with predefined options.
    Automatically quits the browser after the test.
    """
    driver = create_chrome_driver()
    yield driver
    driver.quit()
