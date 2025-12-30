from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page Object for the shopping cart page.
    Encapsulates all actions and verifications related to the cart.
    """

    # Locators
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")

    def proceed_to_checkout(self):
        """
        Proceed from the cart page to the checkout step one page.
        Uses explicit waits and JS click to ensure React state updates properly.
        """
        # Wait for at least one item to be visible in the cart
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEM))

        # Wait for the checkout button to be visible
        checkout_btn = self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BTN))

        # Click the button via JavaScript to bypass potential React click issues
        self.driver.execute_script("arguments[0].click();", checkout_btn)

        # Wait for the page URL to change to checkout-step-one
        self.wait.until(EC.url_contains("checkout-step-one"))

    def count_items(self) -> int:
        """
        Return the number of items currently in the cart.
        Uses explicit wait to ensure elements are present in the DOM.
        """
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM))
        return len(items)
