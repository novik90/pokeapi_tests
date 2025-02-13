import pytest
from pages.home_page import HomePage
from tests.utils import pokemons_test_data as pokemons


@pytest.mark.UI
class TestUI:
    def test_pokeapi_homepage(self, home_page: HomePage, base_url: str):
        home_page.navigate(base_url)

        home_page.verify_title_contains("PokéAPI")
        home_page.verify_body_contains_text("The RESTful Pokémon API")

    @pytest.mark.parametrize(
        "pokemon_id, pokemon_name",
        pokemons,
    )
    def test_search_pokemon_by_name(
        self, home_page: HomePage, base_url: str, pokemon_id: int, pokemon_name: str
    ):
        home_page.navigate(base_url)

        home_page.search_pokemon_by_name(pokemon_name)
        home_page.verify_body_contains_text(pokemon_name)
