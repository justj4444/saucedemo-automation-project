from playwright.sync_api import Page, expect
from pages.saucedemo_product_page import SaucedemoProductPage
from pages.saucedemo_cart_page import SaucedemoCartPage
from pages.saucedemo_checkout_page import SaucedemoCheckoutPage
from test_data.products import PRODUCTS
from test_data.test_logins import test_logins
import logging

logger = logging.getLogger(__name__)

def test_checkout_invalid_details_captured_error_displayed(logged_in_user: Page, add_products_to_cart) -> None:
    product_page = SaucedemoProductPage(logged_in_user)
    cart_page = SaucedemoCartPage(logged_in_user)
    checkout_page = SaucedemoCheckoutPage(logged_in_user)
    product_page.expect_products_page_loaded()      #assert products page is loaded before selecting any product
    logger.info("Products page is loaded")

    #add all products to cart using fixture
    add_products_to_cart([
        product["name"] for product in PRODUCTS.values()
    ])

    cart_page.click_cart_button()
    cart_page.expect_cart_page_loaded()       #assert cart page is loaded before clicking remove button
    logger.info("Cart page is loaded")
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
        logger.info(f"Verified error message: {error_message}")

    checkout_page.click_cancel_button()       #click cancel button to navigate back to cart page
    cart_page.expect_cart_page_loaded()       #assert cart page is loaded after clicking cancel button
    logger.info("Navigated back to cart page after clicking cancel button")