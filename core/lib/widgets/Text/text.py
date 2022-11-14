from RenderElementInterface import RenderElementInterface
import js
import configparser


class text(RenderElementInterface):
    def __init__(self, data, widget_class, type):
        self._data = data
        self._widget_class = widget_class
        self._type = type

    def render(self) -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')

        data = self._data
        wrapper = js.document.createElement('div')
        wrapper.setAttribute('id', self._widget_class)
        title = js.document.createElement('h3')
        title.innerText = data['label']
        wrapper.appendChild(title)

        body = js.document.createElement('div')
        body.setAttribute('class', 'text-container')
        if self._type == 'two_column':
            body.setAttribute('class', 'two-column')
        body.innerHTML = data['body']

        wrapper.appendChild(body)

        main = js.document.getElementById(config.get('RenderElements', 'id_result'))
        main.appendChild(wrapper)
