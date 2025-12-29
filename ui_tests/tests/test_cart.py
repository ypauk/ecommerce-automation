from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart(browser):
    login = LoginPage(browser)
    login.open("https://www.saucedemo.com")
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(browser)
    assert cart.count_items() == 1
