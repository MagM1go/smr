import asyncio

from somerandom.api import SomeRandomApi
from somerandom.endpoints import Filters

api = SomeRandomApi(Filters(avatar='your-avatar-url', _filter='comrade'))

async def main():
    data = await api.create_request()
    return data

loop = asyncio.get_event_loop()
print(loop.run_until_complete(main()))
