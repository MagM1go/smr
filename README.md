<h1 align="center">Some Random Api wrapper</h1>
<p align="center">Module for work with <a href="https://some-random-api.ml">SomeRandom</a>API</p>
<p align="center">
========

Wrapper for https://some-random-api.ml/

Endpoints: https://some-random-api.ml/endpoints (and in api: category name == endpoint in code (Filters and other))

Installing
--------


#### pip install somerandom_wrapper


Example
--------------

```Python
import asyncio

from somerandom.main import SomeRandomApi

api = SomeRandomApi()

print(asyncio.run(api.animal('dog')))

```

