<h1 align="center">SMR - Some Random Api</h1>
<p align="center">Модуль для работы с <a href="https://some-random-api.ml">Some-Random</a>-API</p>
<p align="center">
========

Wrapper for https://some-random-api.ml/

Endpoints: https://some-random-api.ml/endpoints

Installing
--------


#### pip install smr


Sync Example
--------------

```Python
from smr_py import smr_sync


smr = smr_sync.SMR_client()

print(smr.get_point(
                    category="canvas",
                    name="invert",
                    path="?avatar=https://images-ext-2.discordapp.net/external/0DUf6d_FzJSMhsAXEAoYjtGVbdtvbOa6eM7IeBn6m7g/https/cdn.discordapp.com/avatars/598387707311554570/5eb2fad66a96e41fcb514df8d632a354.png"
    ))

```

Async example
--------------

```Python
from smr_py import smr_async
import asyncio


smr = smr_async.SMR()

async def main():
    print(await smr.get_point(
                            category="canvas", 
                            name="invert",
                            path="?avatar=https://images-ext-2.discordapp.net/external/0DUf6d_FzJSMhsAXEAoYjtGVbdtvbOa6eM7IeBn6m7g/https/cdn.discordapp.com/avatars/598387707311554570/5eb2fad66a96e41fcb514df8d632a354.png"
    ))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
