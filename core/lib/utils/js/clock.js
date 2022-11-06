(function () {

    if (typeof Clock === 'undefined')
        window.Clock = {};
    Clock = Clock.Clock = function () {
    }
    var totalSeconds = 0;

    Clock.timer = function () {
        let d = new Date();
        document.getElementById("time").innerHTML = d.toLocaleTimeString();
    }
    Clock.pad = function (val) {
        var valString = val + "";
        if (valString.length < 2) {
            return "0" + valString;
        } else {
            return valString;
        }
    }
    Clock.session = function () {
        ++totalSeconds;
        let hour = Math.floor(totalSeconds / 3600);
        let minute = Math.floor((totalSeconds - hour * 3600) / 60);
        let seconds = totalSeconds - (hour * 3600 + minute * 60);
        if (hour < 10)
            hour = "0" + hour;
        if (minute < 10)
            minute = "0" + minute;
        if (seconds < 10)
            seconds = "0" + seconds;
        document.getElementById("timer").innerHTML = hour + ":" + minute + ":" + seconds;
    }
    Clock.session_init = function () {
        setInterval(function () {
            Clock.session();
        }, 1000);
    }
    Clock.init = function () {
        setInterval(function () {
            Clock.timer();
        }, 1000);
    }
})();