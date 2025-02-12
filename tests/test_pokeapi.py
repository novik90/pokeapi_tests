import pytest
import requests
from typing import Dict, Any
from package.types import StatusCodeChecker, PokemonData


@pytest.mark.parametrize(
    "pokemon_id, expected_name",
    [
        (1, "bulbasaur"),
        (2, "ivysaur"),
        (3, "venusaur"),
    ],
)
def test_get_pokemon_by_id(
    base_url_api: str,
    pokemon_id: int,
    expected_name: str,
    check_status_code: StatusCodeChecker,
) -> None:
    response: requests.Response = requests.get(f"{base_url_api}pokemon/{pokemon_id}")

    check_status_code(response)

    pokemon_data: PokemonData = response.json()
    assert pokemon_data["name"] == expected_name


@pytest.mark.parametrize(
    "pokemon_id, pokemon_name", [(25, "pikachu"), (132, "ditto"), (43, "oddish")]
)
def test_get_pokemon_by_name(
    base_url_api: str,
    pokemon_id: int,
    pokemon_name: str,
    check_status_code: StatusCodeChecker,
) -> None:
    response: requests.Response = requests.get(f"{base_url_api}pokemon/{pokemon_name}")

    check_status_code(response)

    pokemon_data: PokemonData = response.json()
    assert pokemon_data["id"] == pokemon_id
