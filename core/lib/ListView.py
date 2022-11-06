from ElementInterface import ElementInterface
from pyodide.ffi import create_proxy
import js


class ListView(ElementInterface):
    async def proxy_js_to_pyscpript(self, event) -> None:
        event.srcElement.parentNode.parentNode.remove()
        await self.mediator.notify(self, "data", event.srcElement.parentNode)

    def update(self, data, type='', url='', dataset='', text="") -> None:
        item = js.document.createElement('li')
        anchor = js.document.createElement('a')
        anchor.setAttribute('data-type', type)
        anchor.setAttribute('data-rest', url)
        anchor.setAttribute('data-class', data['class'])
        anchor.innerHTML = '<i></i><strong class="dataset">' + dataset + '<span>' + text + '</span></strong>'
        proxy = create_proxy(self.proxy_js_to_pyscpript)
        anchor.addEventListener('click', proxy)
        list_view = js.document.getElementById('list-view')
        item.append(anchor)
        list_view.prepend(item)
