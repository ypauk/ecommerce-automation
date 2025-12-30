from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Page Object for the login page of the application.
    Encapsulates actions like user authentication and error message retrieval.
    """

    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username: str, password: str):
        """
        Fills in the username and password fields and clicks the login button.

        Args:
            username (str): User's login name
            password (str): User's password
        """
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error(self) -> str:
        """
        Returns the text of the login error message if login fails.

        Returns:
            str: Error message text
        """
        return self.get_text(self.ERROR_MSG)
