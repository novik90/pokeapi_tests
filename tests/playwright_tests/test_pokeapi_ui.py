import pytest
from playwright.sync_api import Page
from tests.playwright_tests.pages.home_page import HomePage


@pytest.mark.UI
class TestUI:
    def test_pokeapi_homepage(self, home_page, base_url):
        home_page.navigate(base_url)

        home_page.verify_title_contains("PokéAPI")
        home_page.verify_body_contains_text("The RESTful Pokémon API")

    @pytest.mark.parametrize(
        "pokemon", ["pikachu", "charmander", "slowpoke", "slowking"]
    )
    def test_search_pokemon_by_name(self, home_page, base_url, pokemon):
        home_page.navigate(base_url)

        home_page.search_pokemon(pokemon)
        home_page.verify_body_contains_text(pokemon)
