from playwright.sync_api import Page, expect

class SaucedemoCheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator("[data-test=\"title\"]")
        self.first_name_input = page.locator("[data-test=\"firstName\"]")
        self.last_name_input = page.locator("[data-test=\"lastName\"]")
        self.postal_code_input = page.locator("[data-test=\"postalCode\"]")
        self.cancel_button = page.locator("[data-test=\"cancel\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")

    def expect_title_visible(self) -> None:
        expect(self.title).to_be_visible()

    def expect_first_name_input_visible(self) -> None:
        expect(self.first_name_input).to_be_visible()

    def expect_last_name_input_visible(self) -> None:
        expect(self.last_name_input).to_be_visible()

    def expect_postal_code_input_visible(self) -> None:
        expect(self.postal_code_input).to_be_visible()

    def expect_cancel_button_visible(self) -> None:
        expect(self.cancel_button).to_be_visible()

    def expect_continue_button_visible(self) -> None:
        expect(self.continue_button).to_be_visible()

    def fill_first_name(self, first_name: str) -> None:
        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name: str) -> None:
        self.last_name_input.fill(last_name)

    def fill_zip_code(self, zip_code: str) -> None:
        self.postal_code_input.fill(zip_code)

    def fill_valid_checkout_info(self) -> None:
        self.fill_first_name("Test")
        self.fill_last_name("Testing")
        self.fill_zip_code("12345")

    def click_continue_button(self) -> None:
        self.continue_button.click()

    def click_cancel_button(self) -> None:
        self.cancel_button.click()

    def expect_error_message_text(self, expected_text: str) -> None:
        expect(self.page.locator("[data-test=\"error\"]")).to_have_text(expected_text)
