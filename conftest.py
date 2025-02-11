import pytest
import requests
from package.types import StatusCodeChecker


@pytest.fixture
def base_url() -> str:
    return "https://pokeapi.co/api/v2/"


@pytest.fixture
def check_status_code() -> StatusCodeChecker:
    def _check_status_code(
        response: requests.Response, expected_code: int = 200
    ) -> None:
        assert (
            response.status_code == expected_code
        ), f"Ожидался код ответа {expected_code}, но получен {response.status_code}"

    return _check_status_code
