from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    THANK_YOU_MSG = (By.CLASS_NAME, "complete-header")

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

    def fill_form(self, first, last, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.ZIP_CODE, zip_code)
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()

        #Дополнительно: перед заполнением формы можно вывести для отладки, gпотом удалить:
        print("URL BEFORE FILL_FORM:", self.driver.current_url)

        # 🔥 ждём вторую страницу
        self.wait.until(EC.url_contains("checkout-step-two"))

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()
        self.wait.until(EC.url_contains("complete"))

    def get_thank_you_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.THANK_YOU_MSG)
        ).text

