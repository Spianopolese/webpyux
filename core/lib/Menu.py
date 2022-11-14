from pyodide.ffi import create_proxy
from typing import List
from ElementInterface import ElementInterface
import js


class Menu(ElementInterface):

    def __init__(self, data, menu) -> None:
        self.data = data
        self.menu = js.document.getElementById(menu)

    async def proxy_js_to_pyscpript(self, event) -> None:
        await self.mediator.notify(self, 'data', event.srcElement)

    def generateHTML(self, element, label='', rest_url='', widget_class='', type='', last=False) -> None:
        item = js.document.createElement(element)
        if element == 'li':
            anchor = js.document.createElement('a')
            if rest_url != '':
                anchor.setAttribute('data-widget_class', widget_class)
                if len(type) > 0:
                    anchor.setAttribute('data-type', type)
                anchor.setAttribute('data-rest', rest_url)
            if last:
                icon = js.document.createElement('i')
                icon.classList.add('fa-solid')
                icon.classList.add('fa-chevron-right')
                text = js.document.createElement('span')
                text.innerText = label
                anchor.append(text)
                anchor.append(icon)
            else:
                anchor.innerText = label
            item.append(anchor)
            if rest_url != "":
                proxy = create_proxy(self.proxy_js_to_pyscpript)
                anchor.addEventListener('click', proxy)
        else:
            item.innerText = label
        return item

    def iterateMenu(self, data, parent) -> None:
        for key, value in data.items():
            if type(value) == type(dict()):
                if 'dataset' in value:
                    item = self.generateHTML('li', value['label'], '', '', True)
                    sub_menu = self.generateHTML('ul', '')
                    parent.append(item)
                    item.append(sub_menu)
                    self.iterateMenu(value['dataset'], sub_menu)
                if 'widgets' in value:
                    item = self.generateHTML('span', value['label'])
                    parent.append(item)
                    sub_menu = self.generateHTML('ul', '')
                    for val in value['widgets']:
                        widget_type = val['type'] if 'type' in val else ''
                        widget = self.generateHTML('li', val['label'], val['url'], val['class'], widget_type)
                        sub_menu.append(widget)
                    parent.append(sub_menu)
                else:
                    if 'url' in value:
                        widget_type = value['type'] if 'type' in value else ''
                        simple_element = self.generateHTML('li', value['label'], value['url'], value['class'],
                                                           widget_type)
                        parent.append(simple_element)

    def render(self) -> None:
        self.iterateMenu(self.data, self.menu)
