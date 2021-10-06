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


print(smr_sync.SMR_client().get_point(category="canvas", name="invert", path="?avatar='url'"))
```





Async example
--------------

```Python
from smr_py import smr_async


async def main():
	print(smr_sync.SMR().get_point(category="canvas", name="invert", path="?avatar='url'"))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
