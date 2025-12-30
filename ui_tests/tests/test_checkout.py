from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
# 🔎 БЫСТРАЯ ПРОВЕРКА
from selenium.webdriver.common.by import By

def test_checkout_process(browser):
    # LOGIN
    login = LoginPage(browser)
    login.open("https://www.saucedemo.com")
    login.login("standard_user", "secret_sauce")

    # INVENTORY
    inventory = InventoryPage(browser)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # CART
    cart = CartPage(browser)
    cart.proceed_to_checkout()

    # CHECKOUT
    checkout = CheckoutPage(browser)
    checkout.fill_form_and_continue("John", "Doe", "12345")
    checkout.finish_order()

    # ASSERT
    assert "Thank you" in checkout.get_thank_you_message()

