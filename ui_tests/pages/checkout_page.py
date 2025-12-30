from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    THANK_YOU_MSG = (By.CLASS_NAME, "complete-header")

    def fill_form_and_continue(self, first, last, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)

        self.driver.find_element(*self.CONTINUE_BTN).click()

        # 💥 ВАЖНО: ждём именно URL
        self.wait.until(EC.url_contains("checkout-step-two"))

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()
        self.wait.until(EC.url_contains("checkout-complete"))

    def get_thank_you_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.THANK_YOU_MSG)
        ).text
