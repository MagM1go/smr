import asyncio
from typing import Optional

import aiohttp

from .errors import *


class SMR:

    def __init__(self, loop: asyncio.AbstractEventLoop=None):
        if loop is None:
            loop = asyncio.get_event_loop()

        self._session = aiohttp.ClientSession(
            loop=loop
        )
        self.__url = "https://some-random-api.ml"


    async def get_point(self, category: str=None, name: str=None, path: str=None):
        """
        Examples:

        await smr_async.SMR().get_point(category="canvas", path="?avatar='avatar_url'..."
        """
        async with self._session.get(f'{self.__url}/{name}' if None in (category, path) else f'{self.__url}/{category}/{name}' if path == None else f'{self.__url}/{category}/{name}' + path) as res:
            if res.ok:
                try:
                    a = await res.json()
                except:
                    a = str(res.url)
            else:
                raise NotFoundError("Не было найдено данной категории/имя и прочего. Проверьте путь ещё раз или же правильность написания пути/ссылок.")
            return a