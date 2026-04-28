from playwright.sync_api import Page, expect

class SaucedemoCheckoutCompletePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator("[data-test=\"title\"]")
        self.pony_express = page.locator("[data-test=\"pony-express\"]")
        self.complete_header = page.locator("[data-test=\"complete-header\"]")
        self.complete_text = page.locator("[data-test=\"complete-text\"]")
        self.back_to_products = page.locator("[data-test=\"back-to-products\"]")

    def expect_title_visible(self) -> None:
        expect(self.title).to_have_text("Checkout: Complete!")

    def expect_pony_express_visible(self) -> None:
        expect(self.pony_express).to_be_visible()

    def expect_complete_header_visible(self) -> None:
        expect(self.complete_header).to_be_visible()

    def expect_complete_text_visible(self) -> None:
        expect(self.complete_text).to_be_visible()

    def expect_back_to_products_visible(self) -> None:
        expect(self.back_to_products).to_be_visible()

    def click_back_to_products(self) -> None:
        self.back_to_products.click()

    def checkout_complete_page_loaded(self) -> None:
        self.expect_title_visible()