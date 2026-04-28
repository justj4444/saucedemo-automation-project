from playwright.sync_api import Page, expect
from conftest import page
from pages.saucedemo_product_page import SaucedemoProductPage
from pages.saucedemo_cart_page import SaucedemoCartPage
from pages.saucedemo_checkout_page import SaucedemoCheckoutPage
from test_data.products import PRODUCTS
from test_data.test_logins import test_logins

def test_checkout_invalid_details_captured_error_displayed(logged_in_user: Page, add_products_to_cart: Page) -> None:
    product_page = SaucedemoProductPage(logged_in_user)
    cart_page = SaucedemoCartPage(logged_in_user)
    checkout_page = SaucedemoCheckoutPage(logged_in_user)
    product_page.expect_products_page_loaded()      #assert products page is loaded before selecting any product
    add_products_to_cart(['backpack',
                          'bike light',
                          'fleece jacket',
                          'bolt t-shirt',
                          'Test.allTheThings() T-Shirt (Red)',
                          'sauce labs onesie'])      #add products to cart using fixture

    cart_page.click_cart_button()
    cart_page.expect_cart_page_loaded()       #assert cart page is loaded before clicking remove button
    cart_page.click_checkout_button()       #click checkout button to initiate checkout process

    for user in test_logins.values():
        first_name = user["first_name"]
        last_name = user["last_name"]
        zip_code = user["zip_code"]
        error_message = user["error_message"]

        checkout_page.fill_first_name(first_name)       #fill first name input on checkout page
        checkout_page.fill_last_name(last_name)       #fill last name input on checkout page
        checkout_page.fill_zip_code(zip_code)       #fill postal code input on checkout page
        checkout_page.click_continue_button()       #click continue button to proceed to next step of checkout process
        checkout_page.expect_error_message_text(error_message)       #assert error message is visible when invalid details are entered in checkout form
        print(f"Verified error message: {error_message}")

    checkout_page.click_cancel_button()       #click cancel button to navigate back to cart page
    cart_page.expect_cart_page_loaded()       #assert cart page is loaded after clicking cancel button
