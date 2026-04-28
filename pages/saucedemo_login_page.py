from playwright.sync_api import Page, expect

class SaucedemoLoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")

    def goto(self) -> None:
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        self.username_input.click()
        self.username_input.fill(username)
        self.username_input.press("Tab")
        self.password_input.fill(password)
        self.login_button.click()