from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Page Object for the checkout process.
    Encapsulates all interactions on the checkout pages.
    """

    # Locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    THANK_YOU_MSG = (By.CLASS_NAME, "complete-header")

    def fill_form_and_continue(self, first: str, last: str, zip_code: str):
        """
        Fill in user information on the checkout step one page and proceed to step two.
        Uses explicit waits to ensure fields are interactable.
        """
        # Wait until first name field is visible
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

        # Fill in the input fields
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)

        # Click Continue to go to step two
        self.driver.find_element(*self.CONTINUE_BTN).click()

        # Wait for URL to contain checkout-step-two
        self.wait.until(EC.url_contains("checkout-step-two"))

    def finish_order(self):
        """
        Click the Finish button on checkout step two and wait for completion page.
        """
        # Wait until Finish button is clickable and click
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

        # Wait until URL contains checkout-complete
        self.wait.until(EC.url_contains("checkout-complete"))

    def get_thank_you_message(self) -> str:
        """
        Retrieve the thank you message after completing the checkout.
        """
        return self.wait.until(
            EC.visibility_of_element_located(self.THANK_YOU_MSG)
        ).text
