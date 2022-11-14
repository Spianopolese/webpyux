from pydoc import locate
from Connector import Connector
from ElementInterface import ElementInterface
from RenderElementInterface import RenderElementInterface
import json
import js
import configparser


class Result(ElementInterface):
    data = []

    def update(self, data, widget_class, type) -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')
        js.document.getElementById(config.get('RenderElements', 'id_result')).innerHTML = ""
        element_class = locate(widget_class + '.' + widget_class)
        element = element_class(data, widget_class, type)
        element.render()
