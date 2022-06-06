import asyncio

from somerandom.main import SomeRandomApi

api = SomeRandomApi()

async def main():
    data = await api.filters(_filter='gay', avatar='your-avatar-url')
    return data

loop = asyncio.get_event_loop()
print(loop.run_until_complete(main()))
