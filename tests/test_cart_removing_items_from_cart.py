from playwright.sync_api import Page, expect
from pages.saucedemo_product_page import SaucedemoProductPage
from pages.saucedemo_cart_page import SaucedemoCartPage
from test_data.products import PRODUCTS
import logging

logger = logging.getLogger(__name__)

def test_cart_remove_items_from_cart(logged_in_user: Page, add_products_to_cart) -> None:
    product_page = SaucedemoProductPage(logged_in_user)
    cart_page = SaucedemoCartPage(logged_in_user)
    product_page.expect_products_page_loaded()      #assert products page is loaded before selecting any product    
    logger.info("Products page is loaded")
    
    #add all products to cart using fixture
    add_products_to_cart([
        product["name"] for product in PRODUCTS.values()
    ])

    cart_page.click_cart_button()
    cart_page.expect_cart_page_loaded()       #assert cart page is loaded before clicking remove button
    logger.info("Cart page is loaded")
    for product in PRODUCTS.values():
        name = product["name"]
        expect(cart_page.item_remove_button(name)).to_be_visible()       #assert remove button is visible for the product in cart
        cart_page.click_remove_button(name)       #click remove button to remove product from cart
        expect(cart_page.item_remove_button(name)).not_to_be_visible()       #assert remove button is not visible after removing product from cart
        logger.info(f"Removed {name} from cart")
