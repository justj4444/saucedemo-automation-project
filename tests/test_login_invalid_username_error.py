from playwright.sync_api import Page, expect
from pages.saucedemo_login_page import SaucedemoLoginPage

def test_login_invalid_username_error(page: Page) -> None:
    login_page = SaucedemoLoginPage(page)
    login_page.goto()
    login_page.login("test_test", "test_test")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")   #assert error message is visible when invalid username is entered in login form
    print("Verified error message for invalid username")
