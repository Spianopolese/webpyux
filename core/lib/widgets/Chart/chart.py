from RenderElementInterface import RenderElementInterface
import js
import configparser
from js import BarChart
from pyodide.ffi import create_proxy
import json


class chart(RenderElementInterface):
    def __init__(self, data, type, category):
        self._data = data
        self._category = category
        self._type = type

    def render(self) -> None:
        bar_chart_class = create_proxy(BarChart.new(json.dumps(self._data['data'])))
        proxy_init = create_proxy(bar_chart_class.init(str(self._type)))
        proxy_init.destroy()
        bar_chart_class.destroy()
