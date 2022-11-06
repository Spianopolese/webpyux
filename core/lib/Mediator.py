from MediatorInterface import MediatorInterface
from ListView import ListView
from Menu import Menu
from Result import Result
from AppInfo import AppInfo
from Connector import Connector
import configparser


class Mediator(MediatorInterface):
    def __init__(self, menu: Menu, list_view: ListView, result: Result, app_info: AppInfo) -> None:
        self._menu = menu
        self._menu.mediator = self
        self._list = list_view
        self._list.mediator = self
        self._result = result
        self._result.mediator = self
        self._app_info = app_info
        self._app_info.mediator = self

    async def getData(self, url) -> dict:
        connector = Connector(url)
        return await connector.get()

    async def notify(self, sender: object, event: str, src_element) -> None:
        if event == "data":
            data = await self.getData(src_element.dataset.rest)
            self._list.update(data, src_element.dataset.type, src_element.dataset.rest, data['list_view_dataset'],
                              data['list_view_label'])
            self._result.update(data, src_element.dataset.type)
            self._app_info.update(str(data['list_view_dataset']), data['size'])
