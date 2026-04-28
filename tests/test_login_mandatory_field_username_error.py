from playwright.sync_api import Page, expect
from pages.saucedemo_login_page import SaucedemoLoginPage

def test_login_mandatory_field_username_error(page: Page) -> None:
    login_page = SaucedemoLoginPage(page)
    login_page.goto()
    login_page.login("", "")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username is required")  #assert error message is visible when username field is left empty in login form
    print("Verified error message for mandatory username field")
