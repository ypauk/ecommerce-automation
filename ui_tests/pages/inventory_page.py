from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """
    Page Object for the inventory (products) page.
    Encapsulates actions like adding items to cart and navigating to the cart page.
    """

    # Locators
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_item_to_cart(self):
        """
        Clicks 'Add to Cart' on the first item and waits for the cart badge to appear.
        """
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()
        # Wait until the cart badge updates to indicate item is added
        self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))

    def go_to_cart(self):
        """
        Clicks on the cart icon to navigate to the cart page and waits for the URL to change.
        """
        cart_icon = self.wait.until(EC.visibility_of_element_located(self.CART_ICON))
        # Use JS click to avoid React rendering issues
        self.driver.execute_script("arguments[0].click();", cart_icon)
        self.wait_for_url("cart")
