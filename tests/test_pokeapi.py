import requests
import pytest


@pytest.mark.parametrize(
    "pokemon_id, expected_name",
    [
        (1, "bulbasaur"),
        (2, "ivysaur"),
        (3, "venusaur"),
    ],
)
def test_get_pokemon_by_id(base_url, pokemon_id, expected_name):
    response = requests.get(f"{base_url}pokemon/{pokemon_id}")

    assert response.status_code == 200
    assert response.json()["name"] == expected_name


def test_get_pokemon_by_name(base_url):
    pokemon_name = "pikachu"
    response = requests.get(f"{base_url}pokemon/{pokemon_name}")

    assert response.status_code == 200
    assert response.json()["name"] == pokemon_name
