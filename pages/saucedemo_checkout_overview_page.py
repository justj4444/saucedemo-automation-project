from playwright.sync_api import Page, expect

class SaucedemoCheckoutOverviewPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator("[data-test=\"title\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")

    def expect_title_visible(self) -> None:
        expect(self.title).to_have_text("Checkout: Overview")

    def expect_finish_button_visible(self) -> None:
        expect(self.finish_button).to_be_visible()

    def click_finish_button(self) -> None:
        self.finish_button.click()

    def checkout_overview_page_loaded(self) -> None:
        self.expect_title_visible()
        self.expect_finish_button_visible()

    def get_products_in_checkout_overview(self) -> dict:
        products_locator = self.page.locator(".cart_item")
        product_count = products_locator.count()
        checkout_list = {}
        for i in range(product_count):
            item = products_locator.nth(i)

            name = item.locator(".inventory_item_name").inner_text().strip()
            description = item.locator(".inventory_item_desc").inner_text().strip()
            price = item.locator(".inventory_item_price").inner_text().strip()
            
            checkout_list[name] = {
                "description": description,
                "price": price
                }   
        return checkout_list
    
    def checkout_overview_calculate_total_price(self) -> float:
        products_locator = self.page.locator(".cart_item")
        product_count = products_locator.count()
        total_price = 0.0
        for i in range(product_count):
            item = products_locator.nth(i)
            price_text = item.locator(".inventory_item_price").inner_text().strip()
            price = float(price_text.replace("$", ""))
            total_price += price
        return total_price
    