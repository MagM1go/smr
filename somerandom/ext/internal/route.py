from typing import Literal
from dataclasses import dataclass

URL = "https://some-random-api.ml"

@dataclass(frozen=True)
class Route:
    method: Literal['GET', 'POST', 'PUT', 'PATCH']
    path: str

    def create_url(self):
        return URL + self.path
