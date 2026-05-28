from playwright.sync_api import Page, expect
from pages.saucedemo_login_page import SaucedemoLoginPage
import logging

logger = logging.getLogger(__name__)

def test_login_invalid_password_error(page: Page) -> None:
    login_page = SaucedemoLoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "test_test")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")   #assert error message is visible when invalid password is entered in login form
    logger.info("Verified error message for invalid password")
