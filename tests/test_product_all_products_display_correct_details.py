from playwright.sync_api import Page, expect
from pages.saucedemo_product_page import SaucedemoProductPage
from test_data.products import PRODUCTS
import logging

logger = logging.getLogger(__name__)

def test_all_products_display_correct_details(logged_in_user: Page) -> None:
    product_page = SaucedemoProductPage(logged_in_user)
    product_page.expect_products_page_loaded()      #assert products page is loaded before selecting any product

    for product in PRODUCTS.values():
        name = product["name"]
        description = product["description"]
        price = product["price"]

        product_page.click_product_title(name)      #select product by name
        expect(product_page.product_name).to_be_visible()       #assert product name is visible on product details page
        product_page.expect_product_name_visible()
        logger.info(f"Selected {name} and navigated to product details page")
        
        expect(product_page.product_name).to_have_text(name)    #assert product name is correct on product details page
        expect(product_page.product_description).to_have_text(description)  #assert product description is correct on product details page
        expect(product_page.product_price).to_have_text(price)  #assert product price is correct on product details page
        logger.info(f"Verified {name} details are displayed correctly on product details page")
        expect(product_page.add_to_cart_button).to_be_visible() #assert add to cart button is visible on product details page
        
        product_page.click_back_to_products()       #navigate back to products page before selecting next product
        product_page.expect_products_page_loaded()      #assert products page is loaded before selecting next product