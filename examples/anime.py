import asyncio

from somerandom.api import SomeRandomApi
from somerandom.endpoints import Anime

api = SomeRandomApi(Anime(action='hug'))

async def main():
    data = await api.create_request()
    return data

loop = asyncio.get_event_loop()
print(loop.run_until_complete(main()))
