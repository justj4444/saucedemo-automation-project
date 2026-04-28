from playwright.sync_api import Page, expect


class SaucedemoCartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator("[data-test=\"title\"]")
        self.item_name = page.locator("[data-test=\"inventory-item-name\"]")
        self.item_description = page.locator("[data-test=\"inventory-item-desc\"]")
        self.item_price = page.locator("[data-test=\"inventory-item-price\"]")
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")
        self.remove_button = page.locator("[data-test=\"remove\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")

    def expect_title_visible(self) -> None:
        expect(self.title).to_be_visible()

    def cart_item_by_name(self, product_name: str):
        return self.page.locator(".cart_item").filter(has=self.page.locator(".inventory_item_name", has_text=product_name))

    def expect_item_name_visible(self, product_name: str) -> None:
        expect(self.page.locator(".inventory_item_name", has_text= product_name)).to_have_text(product_name)

    def expect_item_description_visible(self, product_name: str, product_description: str) -> None:
        cart_item = self.cart_item_by_name(product_name)
        expect(cart_item.locator(".inventory_item_desc", has_text= product_description)).to_have_text(product_description)

    def expect_item_price_visible(self, product_name: str, product_price: str) -> None:
        cart_item = self.cart_item_by_name(product_name)
        expect(cart_item.locator(".inventory_item_price", has_text= product_price)).to_have_text(product_price)

    def click_cart_button(self) -> None:
        self.cart_button.click()
    
    def expect_cart_page_loaded(self) -> None:
        expect(self.title).to_be_visible()

    def item_remove_button(self, product_name: str):
        return self.page.locator(
            ".cart_item",
            has=self.page.locator(".inventory_item_name", has_text=product_name)
        ).locator("button:has-text('Remove')")

    def click_remove_button(self, product_name: str) -> None:
        self.item_remove_button(product_name).click()
        expect(self.page.locator(".inventory_item_name", has_text=product_name)).not_to_be_visible()

    def click_checkout_button(self) -> None:
        self.checkout_button.click()

    def get_products_in_cart(self) -> dict:
        products_locator = self.page.locator(".cart_item")
        product_count = products_locator.count()
        cart_list = {}
        for i in range(product_count):
            item = products_locator.nth(i)

            name = item.locator(".inventory_item_name").inner_text().strip()
            description = item.locator(".inventory_item_desc").inner_text().strip()
            price = item.locator(".inventory_item_price").inner_text().strip()

            cart_list[name] = {
                "description": description,
                "price": price
                }   
        return cart_list
    
    def cart_calculate_total_price(self) -> float:
        products_locator = self.page.locator(".cart_item")
        product_count = products_locator.count()
        total_price = 0.0
        for i in range(product_count):
            item = products_locator.nth(i)
            price_text = item.locator(".inventory_item_price").inner_text().strip()
            price = float(price_text.replace("$", ""))
            total_price += price
        return total_price
