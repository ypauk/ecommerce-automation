from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_process(browser):
    """
    End-to-end test for purchasing a product on Saucedemo.

    Steps:
        1. Login with valid credentials.
        2. Add the first item from inventory to the cart.
        3. Proceed to checkout from the cart.
        4. Fill in checkout information and continue.
        5. Finish the order.
        6. Verify the thank-you message is displayed.
    """
    # Step 1: Login
    login_page = LoginPage(browser)
    login_page.open("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add item to cart
    inventory_page = InventoryPage(browser)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    # Step 3: Proceed to checkout
    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

    # Step 4 & 5: Fill checkout form and finish order
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_form_and_continue("John", "Doe", "12345")
    checkout_page.finish_order()

    # Step 6: Assert thank-you message
    thank_you_text = checkout_page.get_thank_you_message()
    assert "Thank you" in thank_you_text, "Checkout failed: Thank you message not found"
