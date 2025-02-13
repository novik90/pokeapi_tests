import pytest
import requests
from requests import Response
from tests.utils import pokemons_test_data as pokemons
from package.types import StatusCodeChecker, PokemonData


@pytest.mark.parametrize(
    "pokemon_id, expected_name",
    pokemons,
)
def test_get_pokemon_by_id(
    base_url_api: str,
    pokemon_id: int,
    expected_name: str,
    check_status_code: StatusCodeChecker,
) -> None:
    response: Response = requests.get(f"{base_url_api}pokemon/{pokemon_id}")

    check_status_code(response)

    pokemon_data: PokemonData = response.json()
    assert pokemon_data["name"] == expected_name


@pytest.mark.parametrize(
    "pokemon_id, pokemon_name",
    pokemons,
)
def test_get_pokemon_by_name(
    base_url_api: str,
    pokemon_id: int,
    pokemon_name: str,
    check_status_code: StatusCodeChecker,
) -> None:
    response: Response = requests.get(f"{base_url_api}pokemon/{pokemon_name}")

    check_status_code(response)

    pokemon_data: PokemonData = response.json()
    assert pokemon_data["id"] == pokemon_id
