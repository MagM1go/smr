from smr_py import smr_async
import asyncio
"""

smr = smr_async.SMR()

async def main():
    print(await smr.get_point(
                            category="canvas", 
                            name="invert",
                            path="?avatar=https://images-ext-2.discordapp.net/external/0DUf6d_FzJSMhsAXEAoYjtGVbdtvbOa6eM7IeBn6m7g/https/cdn.discordapp.com/avatars/598387707311554570/5eb2fad66a96e41fcb514df8d632a354.png"
    ))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())"""

smr = smr_async.SMR()
async def main():
    print(await smr.get_point(category=None, name="joke", path=None))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())