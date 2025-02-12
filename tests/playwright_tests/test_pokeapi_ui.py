from playwright.sync_api import Page, expect


def test_pokeapi_homepage(page: Page, base_url):
    page.goto(base_url)

    expect(page).to_have_title("PokéAPI")

    expect(page.locator("body")).to_contain_text("The RESTful Pokémon API")
