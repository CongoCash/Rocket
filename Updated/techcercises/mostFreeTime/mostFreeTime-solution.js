function MostFreeTime(arr) {

  var aptTimesStart = [], aptTimesEnd = [], sortArr = [];
    var sortStartTimes = [], sortEndTimes = [], justStartTimes = [], justEndTimes = [];
    var loc;

    for (var i = 0; i < arr.length; i++) {
        sortArray = sortCalendar(arr[i].toString());
        aptTimesStart.push(sortArray[0]);
        aptTimesEnd.push(sortArray[1]);
        justStartTimes.push(sortArray[0]);
        justEndTimes.push(sortArray[1]);
    }

    justStartTimes.sort(function(a, b) {return a - b});
    justEndTimes.sort(function(a, b) {return a - b});

    for (var k = 0; k < justStartTimes.length - 1; k++) {
      sortStartTimes.push(justStartTimes[k+1] - justEndTimes[k]);
    }

    sortStartTimes.sort(function(a, b) {return b - a});
    var longestTimeStr = parseInt(sortStartTimes[0] / 60).toString();
    if (longestTimeStr.length < 2) {
        longestTimeStr = "0" + longestTimeStr + ":"  ;
    }
    if ((sortStartTimes[0] % 60).toString().length < 2) {
        longestTimeStr = longestTimeStr + "0" + (sortStartTimes[0] % 60).toString();
    } else {
        longestTimeStr = longestTimeStr + (sortStartTimes[0] % 60).toString();
    }

    return longestTimeStr;

}

function sortCalendar(str) {
    var times, time1, timeap, time2, time2ap, time1min, time2min, tempArr = [];

    times = str.split("-");
    time1 = times[0].slice(0,times[0].length-2).split(":");
    time1ap = times[0][times[0].length-2];
    time2 = times[1].slice(0,times[1].length-2).split(":");
    time2ap = times[1][times[1].length-2];
    time1min = parseInt(time1[0]) * 60 + parseInt(time1[1]);
    time2min = parseInt(time2[0]) * 60 + parseInt(time2[1]);

    if (time1ap === "P" && time1[0] !== "12") {
        time1min += 12 * 60;
    }
    if (time2ap === "P" && time2[0] !== "12") {
        time2min += 12 * 60;
    }

    if (time1ap === "A" && time1[0] === "12") {
        time1min -= (12 * 60);
    }
    if (time2ap === "A" && time2[0] === "12") {
        time2min -= (12 * 60);
    }

    tempArr.push(time1min);
    tempArr.push(time2min);

    return tempArr;
}