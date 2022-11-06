from ElementInterface import ElementInterface
from pyodide.ffi import create_proxy
import js
import math


class AppInfo(ElementInterface):

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def update(self, data='', size='') -> None:
        dataset = js.document.getElementById('current-dataset')
        dataset.innerText = data
        rest_size = int(js.window.rest_size) + int(size)
        js.window.rest_size = rest_size
        data_size = js.document.getElementById('data-size')
        data_size.innerText = self.convert_size(int(rest_size))
