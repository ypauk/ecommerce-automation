from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_first_item_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()
        # Ждём, что бейдж корзины появился
        self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))

    def go_to_cart(self):
        cart_icon = self.wait.until(EC.visibility_of_element_located(self.CART_ICON))
        self.driver.execute_script("arguments[0].click();", cart_icon)
        self.wait_for_url("cart")
