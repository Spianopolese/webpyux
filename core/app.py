from Connector import Connector
from js import localStorage
from User import User
from StatusBar import StatusBar
from Menu import Menu
from ListView import ListView
from Result import Result
from Mediator import Mediator
from AppInfo import AppInfo
from pyodide.ffi import create_proxy
from js import Clock
import configparser
import js
import json

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    user_data = localStorage.getItem('user_data')
    login_url = config.get('Login', 'login_url')
    if not (user_data):
        js.window.location.replace(login_url)
    data = json.loads(user_data)
    if (('access_token' not in data) or ('email' not in data)):
        js.window.location.replace(login_url)
    connector = Connector(config.get('Login', 'auth'))
    response = await connector.get()
    if response['status'] == 200:
        connector = Connector(config.get('RESTUrl', 'url'))
        user = User(data['first_name'], data['last_name'], data['picture'], data['access_token'])
        status_bar = StatusBar(user)
        status_bar.render()
        menu = Menu(await connector.get(), config.get('RenderElements', 'id_main_menu'))
        list_view = ListView()
        result = Result()
        app_info = AppInfo()
        mediator = Mediator(menu, list_view, result, app_info)
        menu.render()
        js.window.rest_size = 0
        create_proxy(Clock.session_init())
    else:
        js.window.location.replace(login_url)
