import requests
from typing import Optional

from .errors import *


class SMR_client:

    def __init__(self):
        self._session = requests
        self.__url = "https://some-random-api.ml"

    def get_point(self, category: Optional[str]=None, name: Optional[str]=None, path: Optional[str]=None):
        request = self._session.get(f'{self.__url}/{category}/{name}' + path)
        if request.ok:
            try:
                data = request.json()
            except:
                data = str(request.url)
        else:
            raise NotFoundError("Не было найдено данной категории/имя и прочего. Проверьте путь ещё раз или же правильность написания пути/ссылок.")
        return data
