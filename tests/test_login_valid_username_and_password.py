from playwright.sync_api import Page, expect
from conftest import page
#from pages.saucedemo_login_page import SaucedemoLoginPage

def test_login_username_and_password(logged_in_user: Page) -> None:
    expect(logged_in_user.locator("[data-test=\"title\"]")).to_be_visible()   #assert products page title is visible after successful login
    print("Verified successful login with valid username and password")