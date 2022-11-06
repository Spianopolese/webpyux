from pydoc import locate
from Connector import Connector
from ElementInterface import ElementInterface
from RenderElementInterface import RenderElementInterface
import json
import js
import configparser


class Result(ElementInterface):
    data = []

    def update(self, data, type) -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')
        js.document.getElementById(config.get('RenderElements', 'id_result')).innerHTML = ""
        class_name = data['class']
        element_class = locate(class_name + '.' + class_name)
        element = element_class(data, type, data['class'])
        element.render()
