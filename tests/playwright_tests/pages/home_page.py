from playwright.sync_api import Page, expect
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_input = page.locator("#url-input")

    def search_pokemon_by_name(self, name: str) -> None:
        self.search_input.fill(name)
        self.search_input.press("Enter")

    def verify_title_contains(self, text: str) -> None:
        expect(self.page).to_have_title(text)

    def verify_body_contains_text(self, text: str) -> None:
        expect(self.page.locator("body")).to_contain_text(text)
