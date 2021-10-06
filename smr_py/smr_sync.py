import requests
from typing import Optional

from .errors import *


class SMR_client:

    def __init__(self):
        self._session = requests
        self._url = "https://some-random-api.ml"

    def get_point(self, category: Optional[str], name: Optional[str], path: Optional[str]):
        request = self._session.get(f'{self._url}/{category}/{name}' + path)
        if request.ok:
            try:
                data = request.json()
            except:
                data = str(request.url)
        else:
            raise NotFoundError("Не было найдено данной категории/имя и прочего. Проверьте путь ещё раз или же правильность написания пути/ссылок.")
        return data
