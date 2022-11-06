from pyodide.ffi import create_proxy
from js import Login
import js
import json
import configparser


def login(event):
    js.event.preventDefault()
    config = configparser.ConfigParser()
    config.read('config.ini')
    email = js.document.getElementById('email').value
    password = js.document.getElementById('password').value
    login_class = create_proxy(Login.new(json.dumps({
        'email': email,
        'password': password,
        'url': config.get('Login', 'url'),
        'pre_auth': config.get('Login', 'pre_auth'),
        'redirect_url': config.get('Login', 'redirect_url')
    })))
    proxy_init = create_proxy(login_class.login())
    proxy_init.destroy()
    login_class.destroy()


if __name__ == "__main__":
    function_proxy = create_proxy(login)
    document.getElementById("submit").addEventListener("click", function_proxy)
