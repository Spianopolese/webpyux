(function () {

    if (typeof WebSocketConnector === 'undefined')
        window.WebSocketConnector = {};

    WebSocketConnector = WebSocketConnector.WebSocketConnector = function (data) {
        this.data = data
    }

    WebSocketConnector.setUpStatusBar = function (wrapper, data) {
        var innerWrapper = document.createElement('div')
        innerWrapper.setAttribute('id', 'websocket-wrapper');

        var status = document.createElement('div')
        status.classList.add('websocket-status');

        let current = document.createElement('span')
        current.classList.add('websocket-server-status');
        status.append(current)

        let url = document.createElement('p')
        url.classList.add('websocket-url');
        url.innerHTML = '<strong>URL:</strong><span>' + data.url + '</span>'
        status.append(url)

        let topic = document.createElement('p')
        topic.classList.add('websocket-url');
        topic.innerHTML = '<strong>Topic:</strong><span>' + data.topic + '</span>'
        status.append(topic)

        innerWrapper.append(status)


        let result = document.createElement('div')
        result.setAttribute('id', 'websocket-result');

        innerWrapper.append(result)
        wrapper.append(innerWrapper)
    }

    WebSocketConnector.prototype.init = function () {
        let data = JSON.parse(this.data)
        let result = document.getElementById('result');
        WebSocketConnector.setUpStatusBar(result, data)
        let websocketWrapper = document.getElementById('websocket-wrapper');
        let websocketResult = document.getElementById('websocket-result');
        const client = mqtt.connect(data.url)
        client.on('connect', function () {
            client.subscribe(data.topic, function (err) {
                if (!err) {
                }
            })
        })

        client.on('message', function (topic, message) {
            var messageWebsocket = document.createElement('p')
            messageWebsocket.innerText = message.toString()
            websocketResult.append(messageWebsocket)
        })

        window.addEventListener('click', function handleClick() {
            if (confirm('Are you sure you want close connection to ' + data.url + '?')) {
                websocketWrapper.innerHTML = '<span>Connection closed. To reinitialize the connection, instantiate the widget again</span>'
                client.end()
                removeEventListener('click', handleClick)
            }
        });
    }
})();