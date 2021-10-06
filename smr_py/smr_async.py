import asyncio
import aiohttp


class SMR:

    MAIN_URL = "https://some-random-api.ml"

    def __init__(self, loop: asyncio.AbstractEventLoop=None):
        if loop is None:
            loop = asyncio.get_event_loop()

        self._session = aiohttp.ClientSession(
            loop=loop
        )

    async def get_fact(self, fact: str):
        async with self._session.get(f'{self.MAIN_URL}/facts/{fact}') as response:
            try:
                return await response.json()
            except Exception as e:
                return e

    async def get_animal(self, animal: str):
        async with self._session.get(f'{self.MAIN_URL}/animal/{animal}') as response:
            try:
                return await response.json()
            except Exception as e:
                return e

    async def get_animal_img(self, animal: str):
        async with self._session.get(f'{self.MAIN_URL}/img/{animal}') as response:
            try:
                return await response.json()
            except Exception as e:
                return e


    async def get_anime(self, reaction: str):
        async with self._session.get(f'{self.MAIN_URL}/animu/{reaction}') as response:
            try:
                return await response.json()
            except Exception as e:
                return e

    async def lyrics(self, lyrics: str):
        async with self._session.get(f'{self.MAIN_URL}/lyrics?title={lyrics}') as response:
            try:
                return await response.json()
            except Exception as e:
                return e

    async def base64(self, code: str, base64_code: str):
        async with self._session.get(f'{self.MAIN_URL}/base64?{"decode" if code == "decode" else "encode"}={base64_code}') as response:
            try:
                return await response.json()
            except Exception as e:
                return e

    async def binary(self, code: str, binary_code: str):
        async with self._session.get(f'{self.MAIN_URL}/binary?{"decode" if code == "decode" else "encode"}={binary_code}') as response:
            try:
                return await response.json()
            except Exception as e:
                return e

    async def joke(self):
        async with self._session.get(f'{self.MAIN_URL}/joke') as response:
            try:
                return await response.json()
            except Exception as e:
                return e

    async def pokedex(self, pokemon: str):
        async with self._session.get(f'{self.MAIN_URL}/pokedex?pokemon={pokemon}') as response:
            try:
                return await response.json()
            except Exception as e:
                return e

    async def gay(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/gay?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def glass(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/glass?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def wasted(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/wasted?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def passed(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/passed?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def jail(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/jail?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def comrade(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/comrade?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def triggered(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/triggered?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def greyscale(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/greyscale?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def invert(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/invert?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def invertgreyscale(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/invertgreyscale?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def brightness(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/brightness?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def threshold(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/threshold?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def sepia(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/sepia?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def red(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/red?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def green(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/green?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def blue(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/blue?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def blurple(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/blurple?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def bluerple2(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/bluerple2?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def pixelate(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/pixelate?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def blur(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/blur?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def youtube_comment(self, avatar_url: str, username: str, comment: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/youtube-comment?avatar={avatar_url}&username={username}&comment={comment}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def tweet(self, avatar_url: str, username: str, comment: str, display_name: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/tweet?avatar={avatar_url}&username={username}&comment={comment}&displayname={display_name}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def stupid(self, avatar_url: str, quote: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/stupid?avatar={avatar_url}&dog={quote}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def simp(self, avatar_url: str, quote: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/simp?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def horny(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/horny?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e

    async def lolice(self, avatar_url: str):
        async with self._session.get(f'{self.MAIN_URL}/canvas/lolice?avatar={avatar_url}') as response:
            try:
                return str(response.url)
            except Exception as e:
                return e
