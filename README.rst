SMR - Some Random Api
========

Wrapper for https://some-random-api.ml/

Endpoints: https://some-random-api.ml/endpoints

Installing
--------

.. code:: sh

pip install smr






Sync Example
--------------

.. code:: py

	from smr_py import smr_sync


	print(smr_sync.SMR_client().get_point(category="canvas", name="invert", path="?avatar='url'"))





Async example
--------------

.. code:: py

	from smr_py import smr_async


	async def main():
	  print(smr_sync.SMR().get_point(category="canvas", name="invert", path="?avatar='url'"))

	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())

