.. code:: sh

pip install smr

.. code:: py
from smr_py import smr_sync


print(smr_sync.SMR_client().get_point(category="canvas", name="invert", path="?avatar='url'"))

# ^ Sync version.

from smr_py import smr_async


async def main():
  print(smr_sync.SMR().get_point(category="canvas", name="invert", path="?avatar='url'"))
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# ^ Async version
