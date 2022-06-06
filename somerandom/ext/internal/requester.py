from typing import Literal, Optional
import aiohttp
from abc import ABC, abstractmethod

from .route import Route


class RequesterABC(ABC):
    @abstractmethod
    async def request(self, route: Route) -> Route: ...


class Requester(RequesterABC):

    def __init__(self):
        ...
        
    async def request(self, route: Route) -> dict:
        async with aiohttp.ClientSession().get(route.create_url()) as response:
            try:
                data = await response.json()
            except:
                data = response.url
            finally:
                return data
