import pytest
from ui_tests.core.driver_factory import create_chrome_driver

@pytest.fixture
def browser():
    """
    Pytest fixture для UI тестов.
    Создает Chrome WebDriver с incognito и другими опциями.
    Автоматически закрывает после теста.
    """
    driver = create_chrome_driver()
    yield driver
    driver.quit()
