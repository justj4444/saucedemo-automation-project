from playwright.sync_api import Page, expect


class SaucedemoProductPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator("[data-test=\"title\"]")
        self.product_name = page.locator("[data-test=\"inventory-item-name\"]")
        self.product_description = page.locator("[data-test=\"inventory-item-desc\"]")
        self.product_price = page.locator("[data-test=\"inventory-item-price\"]")
        self.add_to_cart_button = page.locator("[data-test=\"add-to-cart\"]")
        self.back_to_products_button = page.locator("[data-test=\"back-to-products\"]")
        self.number_of_items = page.locator("[data-test=\"shopping-cart-link\"]")

    def expect_products_page_loaded(self) -> None:
        expect(self.title).to_be_visible()

    def click_product_title(self, product_name: str) -> None:
        self.page.locator('[data-test="inventory-item-name"]', has_text = product_name).click()

    def expect_product_name_visible(self) -> None:
        expect(self.product_name).to_be_visible()

    def expect_product_description_visible(self) -> None:
        expect(self.product_description).to_be_visible()

    def expect_product_price_visible(self) -> None:
        expect(self.product_price).to_be_visible()

    def expect_add_to_cart_button_visible(self) -> None:
        expect(self.add_to_cart_button).to_be_visible()

    def click_add_to_cart_button(self) -> None:
        self.page.locator('[data-test="add-to-cart"]', has_text = 'add to cart').click()

    def click_back_to_products(self) -> None:
        self.back_to_products_button.click()

    def expect_number_of_items_in_cart(self, expected_number: int) -> None:
        expect(self.number_of_items).to_have_text(str(expected_number))