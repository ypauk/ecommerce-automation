from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
# 🔎 БЫСТРАЯ ПРОВЕРКА
from selenium.webdriver.common.by import By

def test_checkout_process(browser):
    login = LoginPage(browser)
    login.open("https://www.saucedemo.com")
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)
    inventory.add_first_item_to_cart()
    # 🔎 БЫСТРАЯ ПРОВЕРКА
    print("Cart badge:",
          browser.find_elements(By.CLASS_NAME, "shopping_cart_badge"))
    inventory.go_to_cart()

    print("URL BEFORE CHECKOUT:", browser.current_url)

    cart = CartPage(browser)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(browser)
    checkout.fill_form("John", "Doe", "12345")
    checkout.finish_order()

    assert "Thank you" in checkout.get_thank_you_message()
