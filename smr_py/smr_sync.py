import requests


class SMR_client:

    def __init__(self):
        self._session = requests
        self._url = "https://some-random-api.ml"

    def get_fact(self, fact: str) -> str:
        return self._session.get(f'{self._url}/facts/{fact}').json()

    def get_animal(self, animal: str) -> str:
        return self._session.get(f'{self._url}/animal/{animal}').json()

    def get_animal_img(self, animal: str) -> str:
        return self._session.get(f'{self._url}/img/{animal}').json()

    def get_anime(self, reaction: str) -> str:
        return self._session.get(f'{self._url}/animu/{reaction}').json()

    def lyrics(self, lyrics: str) -> str:
        return self._session.get(f'{self._url}/lyrics?title={lyrics}').json()

    def base64(self, code: str, base64_code: str):
        return self._session.get(f'{self._url}/base64?{"decode" if code == "decode" else "encode"}={base64_code}').json()

    def binary(self, code: str, binary_code: str):
        return self._session.get(f'{self._url}/binary?{"decode" if code == "decode" else "encode"}={binary_code}').json()

    def joke(self):
        return self._session.get(f'{self._url}/joke').json()

    def pokedex(self, pokemon: str):
        return self._session.get(f'{self._url}/pokedex?pokemon={pokemon}').json()

    def gay(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/gay?avatar={avatar_url}').url)

    def glass(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/glass?avatar={avatar_url}').url)

    def wasted(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/wasted?avatar={avatar_url}').url)

    def passed(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/passed?avatar={avatar_url}').url)

    def jail(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/jail?avatar={avatar_url}').url)

    def comrade(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/comrade?avatar={avatar_url}').url)

    def triggered(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/triggered?avatar={avatar_url}').url)

    def invert(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/invert?avatar={avatar_url}').url)

    def greyscale(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/greyscale?avatar={avatar_url}').url)

    def invertgreyscale(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/invertgreyscale?avatar={avatar_url}').url)

    def brightness(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/brightness?avatar={avatar_url}').url)

    def threshold(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/threshold?avatar={avatar_url}').url)

    def sepia(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/sepia?avatar={avatar_url}').url)

    def red(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/red?avatar={avatar_url}').url)

    def blue(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/blue?avatar={avatar_url}').url)

    def blurple(self, avatar_url: str):
        return str(self._session.get(f'{self._url}/canvas/blurple?avatar={avatar_url}').url)
