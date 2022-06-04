import aiohttp


class Route:
    def __init__(self, method: str, url: str) -> None:
        self.method = method
        self.url = url

    async def get_request(self) -> dict:
        response = await aiohttp.ClientSession().request(self.method, self.url)
        try:
            data = await response.json()
        except:
            data = response.url
        finally:
            return data
