from RenderElementInterface import RenderElementInterface
from js import WebSocketConnector
from pyodide.ffi import create_proxy
import js
import configparser
import json


class websocket(RenderElementInterface):
    def __init__(self, data, widget_class, type):
        self._data = data
        self._widget_class = widget_class
        self._type = type

    def render(self) -> None:
        websocket_class = create_proxy(WebSocketConnector.new(json.dumps(self._data['data'])))
        proxy_init = create_proxy(websocket_class.init())
        proxy_init.destroy()
        websocket_class.destroy()
