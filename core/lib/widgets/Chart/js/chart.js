(function () {
    if (typeof BarChart === 'undefined')
        window.BarChart = {};

    BarChart = BarChart.BarChart = function (data) {
        this.data = data
    }

    BarChart.prototype.init = function (type) {
        let wrapper = document.createElement('div')
        wrapper.setAttribute('id', 'chart')
        let canvas = document.createElement('canvas')
        canvas.setAttribute('id', 'bar-chart')
        wrapper.append(canvas)
        document.getElementById('result').append(wrapper)
        const ctx = canvas.getContext('2d');
        let data = JSON.parse(this.data)
        new Chart(ctx, {
            type: type,
            data: data,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
})();