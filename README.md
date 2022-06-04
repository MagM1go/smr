<h1 align="center">Some Random Api wrapper</h1>
<p align="center">Module for work with <a href="https://some-random-api.ml">SomeRandom</a>API</p>
<p align="center">
========

Wrapper for https://some-random-api.ml/

Endpoints: https://some-random-api.ml/endpoints

Installing
--------


#### pip install somerandom_wrapper


Example
--------------

```Python
import asyncio

from somerandom.api import SomeRandomApi
from somerandom.endpoints import Filters

api = SomeRandomApi(Filters(avatar='your-avatar-url', _filter='comrade'))

async def main():
    data = await api.create_request()
    return data

loop = asyncio.get_event_loop()
print(loop.run_until_complete(main()))

```