from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def wait_until_loaded(self):
        # Ждём появления хотя бы одного товара с таймаутом 10 секунд
        self.wait.until(lambda d: len(d.find_elements(*self.CART_ITEMS)) > 0)

    def proceed_to_checkout(self):
        self.wait_until_loaded()

        # Делаем небольшую паузу, чтобы DOM точно успел прогрузиться
        time.sleep(0.3)

        # Ждём, пока кнопка Checkout станет кликабельной
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BTN)
        )
        checkout_button.click()

        # Ждём переход на страницу checkout-step-one
        self.wait_for_url("checkout-step-one")

    def count_items(self):
        self.wait_until_loaded()
        return len(self.driver.find_elements(*self.CART_ITEMS))
