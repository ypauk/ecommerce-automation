from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")

    def proceed_to_checkout(self):
        # 1️⃣ ждём товар
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEM))

        # 2️⃣ ждём кнопку
        checkout_btn = self.wait.until(
            EC.visibility_of_element_located(self.CHECKOUT_BTN)
        )

        # 3️⃣ JS-клик (КЛЮЧЕВО!)
        self.driver.execute_script("arguments[0].click();", checkout_btn)

        # 4️⃣ ждём реальный переход
        self.wait.until(EC.url_contains("checkout-step-one"))

    def count_items(self):
        """Возвращает количество товаров в корзине"""
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM))
        return len(items)