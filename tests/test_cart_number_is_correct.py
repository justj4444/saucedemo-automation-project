from playwright.sync_api import Page, expect
from conftest import page
from pages.saucedemo_product_page import SaucedemoProductPage
from test_data.products import PRODUCTS

def test_cart_number_is_correct(logged_in_user: Page) -> None:
    product_page = SaucedemoProductPage(logged_in_user)
    product_page.expect_products_page_loaded()      #assert products page is loaded before selecting any product
    x = 0

    for product in PRODUCTS.values():
        name = product["name"]
        x += 1

        product_page.click_product_title(name)      #select product by name
        expect(product_page.product_name).to_be_visible()       #assert product name is visible on product details page
        product_page.click_add_to_cart_button()
        expect(product_page.number_of_items).to_be_visible()       #assert number of items in cart is visible after adding product to cart
        product_page.expect_number_of_items_in_cart(x)      #assert number of items in
        
        product_page.click_back_to_products()       #navigate back to products page before selecting next product
        product_page.expect_products_page_loaded()      #assert products page is loaded before selecting next product
        print(f"Number of items in cart after adding {name}: {x}")