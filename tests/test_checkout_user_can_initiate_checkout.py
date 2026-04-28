from playwright.sync_api import Page, expect
from conftest import page
from pages.saucedemo_product_page import SaucedemoProductPage
from pages.saucedemo_cart_page import SaucedemoCartPage
from pages.saucedemo_checkout_page import SaucedemoCheckoutPage
from test_data.products import PRODUCTS

def test_checkout_user_can_initiate_checkout(logged_in_user: Page, add_products_to_cart: Page) -> None:
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

    checkout_page.expect_title_visible()       #assert title is visible on checkout page
    checkout_page.expect_first_name_input_visible()       #assert first name input is visible on checkout page
    checkout_page.expect_last_name_input_visible()       #assert last name input is visible on checkout page
    checkout_page.expect_postal_code_input_visible()       #assert postal code input is visible on  checkout page
    checkout_page.expect_cancel_button_visible()       #assert cancel button is visible on checkout page
    checkout_page.expect_continue_button_visible()       #assert continue button is visible on checkout page
    print("Checkout page is loaded and all elements are visible")