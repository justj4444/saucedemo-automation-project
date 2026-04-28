from playwright.sync_api import Page, expect
from conftest import page
from pages.saucedemo_product_page import SaucedemoProductPage
from pages.saucedemo_cart_page import SaucedemoCartPage
from test_data.products import PRODUCTS

def test_cart_displays_selected_items_correctly(logged_in_user: Page, add_products_to_cart: Page) -> None:
    product_page = SaucedemoProductPage(logged_in_user)
    cart_page = SaucedemoCartPage(logged_in_user)
    product_page.expect_products_page_loaded()      #assert products page is loaded before selecting any product
    
    add_products_to_cart(['backpack',
                          'bike light',
                          'fleece jacket',
                          'bolt t-shirt',
                          'Test.allTheThings() T-Shirt (Red)',
                          'sauce labs onesie'])      #add products to cart using fixture

    cart_page.click_cart_button()   
    cart_page.expect_cart_page_loaded()       #assert cart page is loaded before clicking remove button
    
    for product in PRODUCTS.values():
        name = product["name"]
        description = product["description"]
        price = product["price"]

        cart_page.expect_item_name_visible(name)       #assert product name is visible on cart page
        cart_page.expect_item_description_visible(name, description)       #assert product description is visible on cart page
        cart_page.expect_item_price_visible(name, price)       #assert product price is visible
        print(f"Verified {name} is displayed correctly in cart with description and price")

        cart_page.click_remove_button(name)       #click remove button to remove product from cart
        expect(cart_page.item_remove_button(name)).not_to_be_visible()       #assert remove button is not visible after removing product from cart
