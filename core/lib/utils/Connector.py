from js import localStorage
from pyodide.http import pyfetch
import json
import js
import configparser
import json


class Connector:
    def __init__(self, url) -> None:
        user_data = localStorage.getItem('user_data')
        data = json.loads(user_data)
        self._url = url + '?access_token=' + data['access_token'] + '&email=' + data['email']

    def createLoader(self) -> None:
        config = configparser.ConfigParser()
        config.read('config.ini')

        wrapper = js.document.createElement('div')
        wrapper.setAttribute('id', 'loader-wrapper')
        loader = js.document.createElement('div')
        loader.classList.add('loader')
        loader_inner = js.document.createElement('div')
        loader_inner.classList.add('loader-inner')
        loader.append(loader_inner)
        wrapper.append(loader)
        js.document.getElementById(config.get('RenderElements', 'id_result')).append(wrapper)

    def removeLoader(self) -> None:
        js.document.getElementById('loader-wrapper').remove()

    async def get(self) -> None:
        self.createLoader()
        try:
            res = await pyfetch(url=self._url, method='GET')
            items = await res.json()
            self.removeLoader()
            return items
        except:
            self.removeLoader()
            js.console.error("Error retrieving data from " + self._url)

    async def post(self) -> None:
        try:
            res = await pyfetch(url=self._url, method='GET')
            items = await res.json()
            return items
        except:
            js.console.error("Error retrieving data from " + self._url)
