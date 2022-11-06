(function () {
    if (typeof Login === 'undefined')
        window.Login = {};

    Login = Login.Login = function (data) {
        this.data = JSON.parse(data)
    }

    Login.appendLoader = function () {
        let wrapper = document.createElement('div')
        wrapper.setAttribute('id', 'loader-wrapper')
        let loader = document.createElement('div')
        loader.classList.add('loader')
        let loader_inner = document.createElement('div')
        loader_inner.classList.add('loader-inner')
        loader.append(loader_inner)
        wrapper.append(loader)
        document.body.append(wrapper)
    }
    Login.removeLoader = function () {
        document.getElementById('loader-wrapper').remove()
    }

    Login.prototype.login = function () {
        let data = this.data
        let xhr = new XMLHttpRequest()
        xhr.open('POST', this.data.pre_auth, true)
        xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
        xhr.setRequestHeader('Access-Control-Allow-Origin', '*')
        xhr.send();
        xhr.onload = function () {
            let response = xhr.response
            let xCSRFToken = response
            if (response.length > 0) {
                let postObj = {
                    email: data.email,
                    password: data.password
                }
                let post = JSON.stringify(postObj)
                const url = data.url
                xhr.open('POST', url, true)
                xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
                xhr.setRequestHeader('X-CSRF-Token', xCSRFToken)
                xhr.setRequestHeader('Access-Control-Allow-Origin', '*')
                xhr.send(post);
                Login.appendLoader()
                xhr.onload = function () {
                    let response = JSON.parse(xhr.response)
                    if (response.status === 200) {
                        localStorage.clear();
                        localStorage.setItem('user_data', JSON.stringify(response.user_data));
                        window.location.replace(data.redirect_url);
                    } else {
                        Login.removeLoader()
                        document.getElementById('error').style.display = 'block';
                        document.querySelectorAll('input').forEach((e) => {
                            e.classList.add("error");
                        })
                        console.error("User not found")
                    }
                }
            }
        }
    }
})();