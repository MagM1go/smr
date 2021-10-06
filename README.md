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
		path="?avatar='link'"
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
		path="?avatar='link'"
    ))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
