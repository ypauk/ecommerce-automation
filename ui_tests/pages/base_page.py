from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    BasePage class implements common Selenium WebDriver methods.
    All page objects will inherit from this class to reuse these utilities.
    """

    def __init__(self, driver):
        """
        Initialize the page with a Selenium WebDriver instance.
        A WebDriverWait instance is created for explicit waits.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds default timeout

    def open(self, url: str):
        """
        Open a given URL in the browser.
        """
        self.driver.get(url)

    def wait_for_url(self, partial_url: str):
        """
        Wait until the current URL contains the specified partial string.
        Useful for page navigation verification.
        """
        self.wait.until(EC.url_contains(partial_url))

    def find(self, locator):
        """
        Wait for presence of an element located by `locator` and return it.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """
        Wait until the element is clickable and perform a click action.
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text: str):
        """
        Clear any existing text and type the provided value into the input element.
        """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        """
        Return the visible text of an element.
        """
        return self.find(locator).text
