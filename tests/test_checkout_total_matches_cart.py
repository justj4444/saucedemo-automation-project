from playwright.sync_api import Page, expect
from conftest import page
from pages.saucedemo_product_page import SaucedemoProductPage
from pages.saucedemo_cart_page import SaucedemoCartPage
from pages.saucedemo_checkout_page import SaucedemoCheckoutPage
from pages.saucedemo_checkout_overview_page import SaucedemoCheckoutOverviewPage
from test_data.products import PRODUCTS
import logging

logger = logging.getLogger(__name__)

def test_checkout_total_matches_cart(logged_in_user: Page, add_products_to_cart) -> None:
    product_page = SaucedemoProductPage(logged_in_user)
    cart_page = SaucedemoCartPage(logged_in_user)
    checkout_page = SaucedemoCheckoutPage(logged_in_user)
    checkout_overview_page = SaucedemoCheckoutOverviewPage(logged_in_user)
    product_page.expect_products_page_loaded()      #assert products page is loaded before selecting any product
    logger.info("Products page is loaded")

    #add all products to cart using fixture
    add_products_to_cart([
        product["name"] for product in PRODUCTS.values()
    ])

    cart_page.click_cart_button()
    cart_page.expect_cart_page_loaded()       #assert cart page is loaded before clicking remove button
    logger.info("Cart page is loaded")

    cart_page_products = cart_page.cart_calculate_total_price()      #get total price of products in cart before checkout
    logger.info(f"Total price in cart before checkout: {cart_page_products}")      #get total price of products in cart before checkout

    cart_page.click_checkout_button()       #click checkout button to initiate checkout process

    checkout_page.fill_valid_checkout_info()      #fill checkout info with valid details
    checkout_page.click_continue_button()       #click continue button to proceed to checkout overview page

    checkout_overview_page_products = checkout_overview_page.checkout_overview_calculate_total_price()      #get total price of products in checkout overview page
    logger.info(f"Total price in checkout overview page: {checkout_overview_page_products}")      #get total price of products in checkout overview page

    logger.info("Checking if total prices match")
    assert cart_page_products == checkout_overview_page_products, "Total prices in cart and checkout overview page match"     #assert total prices in cart and checkout overview page are the same after clicking checkout button
