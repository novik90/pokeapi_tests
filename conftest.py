import pytest
import requests
from tests.playwright_tests.pages.home_page import HomePage
from playwright.sync_api import sync_playwright, Browser, Page
from package.types import StatusCodeChecker


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://pokeapi.co/"


@pytest.fixture(scope="session")
def base_url_api(base_url) -> str:
    return f"{base_url}api/v2/"


@pytest.fixture
def check_status_code() -> StatusCodeChecker:
    def _check_status_code(
        response: requests.Response, expected_code: int = 200
    ) -> None:
        assert (
            response.status_code == expected_code
        ), f"Ожидался код ответа {expected_code}, но получен {response.status_code}"

    return _check_status_code


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)
