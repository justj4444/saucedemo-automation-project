from playwright.sync_api import Page, expect
from pages.saucedemo_product_page import SaucedemoProductPage
from pages.saucedemo_cart_page import SaucedemoCartPage
from pages.saucedemo_checkout_page import SaucedemoCheckoutPage
from pages.saucedemo_checkout_overview_page import SaucedemoCheckoutOverviewPage
from pages.saucedemo_checkout_complete_page import SaucedemoCheckoutCompletePage
from test_data.products import PRODUCTS
import logging

logger = logging.getLogger(__name__)

def test_checkout_valid_details_captured(logged_in_user: Page, add_products_to_cart) -> None:
    product_page = SaucedemoProductPage(logged_in_user)
    cart_page = SaucedemoCartPage(logged_in_user)
    checkout_page = SaucedemoCheckoutPage(logged_in_user)
    checkout_overview_page = SaucedemoCheckoutOverviewPage(logged_in_user)
    checkout_complete_page = SaucedemoCheckoutCompletePage(logged_in_user)
    product_page.expect_products_page_loaded()      #assert products page is loaded before selecting any product
    logger.info("Products page is loaded")

    #add all products to cart using fixture
    add_products_to_cart([
        product["name"] for product in PRODUCTS.values()
    ])

    cart_page.click_cart_button()
    cart_page.expect_cart_page_loaded()       #assert cart page is loaded before clicking remove button
    cart_page_products = cart_page.get_products_in_cart()      #get products in cart before checkout
    logger.info(f"Products in cart before checkout: {cart_page_products}")

    cart_page.click_checkout_button()       #click checkout button to initiate checkout process

    checkout_page.fill_valid_checkout_info()      #fill checkout info with valid details
    checkout_page.click_continue_button()       #click continue button to proceed to checkout overview page
    checkout_overview_page.checkout_overview_page_loaded()      #assert checkout overview page is loaded before clicking finish button

    checkout_overview_page_products = checkout_overview_page.get_products_in_checkout_overview()      #get products in checkout overview page
    logger.info(f"Products in checkout overview page: {checkout_overview_page_products}")

    assert cart_page_products == checkout_overview_page_products, "Products in cart and checkout overview page match"     #assert products in cart and checkout overview page are the same after clicking checkout button
    
    checkout_overview_page.click_finish_button()       #click finish button to complete checkout process
    checkout_complete_page.checkout_complete_page_loaded()      #assert checkout complete page is loaded after clicking finish button
    checkout_complete_page.expect_pony_express_visible()       #assert pony express image is visible on checkout complete page
    checkout_complete_page.expect_complete_header_visible()       #assert complete header is visible on checkout complete page
    checkout_complete_page.expect_complete_text_visible()       #assert complete text is visible on checkout complete
    checkout_complete_page.expect_back_to_products_visible()       #assert back to products button is visible on checkout complete page
    checkout_complete_page.click_back_to_products()       #click back to products button to navigate back to products page
    product_page.expect_products_page_loaded()      #assert products page is loaded after clicking back to
    logger.info("Checkout process completed successfully and user navigated back to products page")
    