from .request import Route

GET = "GET"
URL = "https://some-random-api.ml"

class SomeRandomApi:

    def __init__(self, api_object):
        self.object = api_object
        self.route = Route(GET, URL + self.object.get_path())

    async def create_request(self):
        return await self.route.get_request()
