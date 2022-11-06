from pyodide.ffi import create_proxy
from js import Clock
from js import localStorage
import js
import configparser


class StatusBar:
    def __init__(self, user) -> None:
        self.user = user

    def logOut(self, event):
        localStorage.clear()
        config = configparser.ConfigParser()
        config.read('config.ini')
        js.window.location.replace(config.get('Login', 'login_url'))

    def render(self) -> None:
        user = js.document.getElementById('user')
        picture = js.document.createElement('img')
        picture.src = self.user.getPicture()
        name = js.document.createElement('label')
        name.innerText = 'Hi ' + self.user.getFirstName() + ' ' + self.user.getLastName()
        user.prepend(name)
        user.prepend(picture)
        create_proxy(Clock.init())
        logout_proxy = create_proxy(self.logOut)
        js.document.getElementById('logout').addEventListener("click", logout_proxy)
