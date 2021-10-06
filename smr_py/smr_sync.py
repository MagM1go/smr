import requests
from typing import Literal

from .errors import *


class SMR_client:

    def __init__(self):
        self._session = requests
        self.__url = "https://some-random-api.ml"

    def get_point(self, category: str=None, name: str=None, path: str=None):
        request = self._session.get(f'{self.__url}/{name}' if None in (category, path) else f'{self.__url}/{category}/{name}' if path == None else f'{self.__url}/{category}/{name}' + path)
        if request.ok:
            try:
                data = request.json()
            except:
                data = str(request.url)
        else:
            raise NotFoundError("Не было найдено данной категории/имя и прочего. Проверьте путь ещё раз или же правильность написания пути/ссылок.")
        return data
