import requests
from typing import Callable, Dict, Any

StatusCodeChecker = Callable[[requests.Response, int], None]
PokemonData = Dict[str, Any]
