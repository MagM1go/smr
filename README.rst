.. code:: sh

pip install smr

.. code:: py
from smr_py import smr_sync


print(smr_sync.SMR_client().invert(avatar_url="avatar_url"))

# ^ Sync version.

from smr_py import smr_async


async def main():
  print(smr_sync.SMR().invert(avatar_url="avatar"))
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
