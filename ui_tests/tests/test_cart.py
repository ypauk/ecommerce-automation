from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart(browser):
    """
    Test to verify adding an item to the cart works correctly.

    Steps:
        1. Open Saucedemo login page.
        2. Login with valid credentials.
        3. Add the first item from inventory to the cart.
        4. Navigate to the cart page.
        5. Assert that the cart contains exactly 1 item.
    """
    # Login
    login_page = LoginPage(browser)
    login_page.open("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    # Add item to cart
    inventory_page = InventoryPage(browser)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    # Verify cart
    cart_page = CartPage(browser)
    assert cart_page.count_items() == 1, "Cart does not contain exactly 1 item"
