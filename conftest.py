import pytest
import logging
from playwright.sync_api import sync_playwright

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_execution.log"),
        logging.StreamHandler()
    ]
)

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def logged_in_user(page):
    from pages.saucedemo_login_page import SaucedemoLoginPage
    login_page = SaucedemoLoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    return page

@pytest.fixture
def add_products_to_cart(logged_in_user):
    def _add(products):
        from pages.saucedemo_product_page import SaucedemoProductPage
        product_page = SaucedemoProductPage(logged_in_user)
        for product in products:
            product_page.click_product_title(product)
            product_page.click_add_to_cart_button()
            product_page.click_back_to_products()
            product_page.expect_products_page_loaded()
    return _add

    