const width_threshold = 480;
function drawLineChart() {
    if ($("#lineChart").length) {
        ctxLine = document.getElementById("lineChart").getContext("2d");
        optionsLine = {
            scales: {
                yAxes: [
                    {
                        scaleLabel: {
                            display: true,
                            labelString: "Hits"
                        }
                    }
                ]
            }
        };

        // Set aspect ratio based on window width
        optionsLine.maintainAspectRatio =
            $(window).width() < width_threshold ? false : true;

        configLine = {
            type: "line",
            data: {
                labels: [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July"
                ],
                datasets: [
                    {
                        label: "Latest Hits",
                        data: [88, 68, 79, 57, 56, 55, 70],
                        fill: false,
                        borderColor: "rgb(75, 192, 192)",
                        lineTension: 0.1
                    },
                    {
                        label: "Popular Hits",
                        data: [33, 45, 37, 21, 55, 74, 69],
                        fill: false,
                        borderColor: "rgba(255,99,132,1)",
                        lineTension: 0.1
                    },
                    {
                        label: "Featured",
                        data: [44, 19, 38, 46, 85, 66, 79],
                        fill: false,
                        borderColor: "rgba(153, 102, 255, 1)",
                        lineTension: 0.1
                    }
                ]
            },
            options: optionsLine
        };

        lineChart = new Chart(ctxLine, configLine);
    }
}

function drawBarChart(score, title, score2, title2, score3, title3) {

    optionsBar = {
        responsive: true,
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Similarity Score"
                    }
                }
            ],
            xAxes: [
                {
                    ticks: {
                        display: false //this will remove only the label
                    }
                }]
        }
    };
    optionsBar.maintainAspectRatio =
        $(window).width() < width_threshold ? false : true;


    ctxBar = document.getElementById("barChart").getContext("2d");
    configBar = {
        type: "bar",
        data: {
            labels: title,//["Red", "Blue", "Yellow", "Green", "Purple", "Orange", "ww", "eee", "www", "sss"],
            datasets: [
                {
                    label: "Score of Similarity",
                    data: score, //[12, 19, 3, 5, 2, 3, 6, 8, 4, 9],
                    backgroundColor: [
                        "rgba(252, 160, 252, 0.2)",
                        "rgba(249, 133, 133, 0.2)",
                        "rgba(255, 206, 86, 0.2)",
                        "rgba(75, 142, 192, 0.2)",
                        "rgba(255, 99, 132, 0.2)",
                        "rgba(54, 162, 235, 0.2)",
                        "rgba(255, 26, 86, 0.2)",
                        "rgba(75, 192, 192, 0.2)",
                        "rgba(153, 102, 255, 0.2)",
                        "rgba(255, 159, 64, 0.2)"
                    ],
                    borderColor: [
                        "rgba(252, 160, 252, 1)",
                        "rgba(249, 133, 133, 1)",
                        "rgba(255, 206, 86, 1)",
                        "rgba(75, 142, 192, 1)",
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 26, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 102, 255, 1)",
                        "rgba(255, 159, 64, 1)"
                    ],
                    borderWidth: 1
                }
            ]
        },
        options: optionsBar
    };


    ctxBar2 = document.getElementById("barChart2").getContext("2d");
    configBar2 = {
        type: "bar",
        data: {
            labels: title2,//["Red", "Blue", "Yellow", "Green", "Purple", "Orange", "ww", "eee", "www", "sss"],
            datasets: [
                {
                    label: "Score of Similarity",
                    data: score2, //[12, 19, 3, 5, 2, 3, 6, 8, 4, 9],
                    backgroundColor: [
                        "rgba(255, 99, 132, 0.2)",
                        "rgba(54, 162, 205, 0.2)",
                        "rgba(255, 226, 86, 0.2)",
                        "rgba(75, 192, 192, 0.2)",
                        "rgba(153, 12, 255, 0.2)",
                        "rgba(57, 162, 235, 0.2)",
                        "rgba(205, 206, 86, 0.2)",
                        "rgba(75, 192, 122, 0.2)",
                        "rgba(153, 102, 25, 0.2)",
                        "rgba(225, 159, 64, 0.2)"
                    ],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 205, 1)",
                        "rgba(255, 226, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 12, 255, 1)",
                        "rgba(57, 162, 235, 1)",
                        "rgba(205, 206, 86, 1)",
                        "rgba(75, 192, 122, 1)",
                        "rgba(153, 102, 25, 1)",
                        "rgba(225, 159, 64, 1)"
                    ],
                    borderWidth: 1
                }
            ]
        },
        options: optionsBar
    };

    ctxBar3 = document.getElementById("barChart3").getContext("2d");
    configBar3 = {
        type: "bar",
        data: {
            labels: title3,//["Red", "Blue", "Yellow", "Green", "Purple", "Orange", "ww", "eee", "www", "sss"],//title3,// ["Red", "Blue", "Yellow", "Green", "Purple", "Orange", "ww", "eee", "www", "sss"],
            datasets: [
                {
                    label: "Score of Similarity",
                    data: score3, //[12, 19, 3, 5, 2, 3, 6, 8, 4, 9],
                    backgroundColor: [
                        "rgba(114, 248, 11, 0.2)",
                        "rgba(54, 62, 205, 0.2)",
                        "rgba(255, 226, 86, 0.2)",
                        "rgba(75, 102, 192, 0.2)",
                        "rgba(153, 12, 155, 0.2)",
                        "rgba(57, 132, 235, 0.2)",
                        "rgba(205, 206, 86, 0.2)",
                        "rgba(70, 192, 142, 0.2)",
                        "rgba(11, 211, 248, 0.2)",
                        "rgba(248, 11 189, 0.2)"
                    ],
                    borderColor: [
                        "rgba(114, 248, 11, 1)",
                        "rgba(54, 62, 205, 1)",
                        "rgba(255, 226, 86, 1)",
                        "rgba(75, 102, 192, 1)",
                        "rgba(153, 12, 155, 1)",
                        "rgba(57, 132, 235, 1)",
                        "rgba(205, 206, 86, 1)",
                        "rgba(70, 192, 142, 1)",
                        "rgba(11, 211, 248, 1)",
                        "rgba(248, 11 189, 1)"
                    ],
                    borderWidth: 1
                }
            ]
        },
        options: optionsBar
    };

    if ($("#barChart").length) {
        barChart = new Chart(ctxBar, configBar);
    }

    if ($("#barChart2").length) {
        barChart2 = new Chart(ctxBar2, configBar2);
    }

    if ($("#barChart3").length) {
        barChart3 = new Chart(ctxBar3, configBar3);
    }

}


function drawPieChart() {
    if ($("#pieChart").length) {
        ctxPie = document.getElementById("pieChart").getContext("2d");
        optionsPie = {
            responsive: true,
            maintainAspectRatio: false
        };

        configPie = {
            type: "pie",
            data: {
                datasets: [
                    {
                        data: [4600, 5400],
                        backgroundColor: [
                            window.chartColors.purple,
                            window.chartColors.green
                        ],
                        label: "Storage"
                    }
                ],
                labels: ["Used: 4,600 GB", "Available: 5,400 GB"]
            },
            options: optionsPie
        };

        pieChart = new Chart(ctxPie, configPie);
    }
}

function updateChartOptions() {
    if ($(window).width() < width_threshold) {
        if (optionsLine) {
            optionsLine.maintainAspectRatio = false;
        }
        if (optionsBar) {
            optionsBar.maintainAspectRatio = false;
        }
    } else {
        if (optionsLine) {
            optionsLine.maintainAspectRatio = true;
        }
        if (optionsBar) {
            optionsBar.maintainAspectRatio = true;
        }
    }
}

function updateLineChart() {
    if (lineChart) {
        lineChart.options = optionsLine;
        lineChart.update();
    }
}

function updateBarChart() {
    if (barChart2) {
        barChart2.options = optionsBar;
        barChart2.update();
    }
}

function reloadPage() {
    setTimeout(function () {
        window.location.reload();
    }); // Reload the page so that charts will display correctly
}

function drawCalendar() {
    if ($("#calendar").length) {
        $("#calendar").fullCalendar({
            height: 400,
            events: [
                {
                    title: "Meeting",
                    start: "2018-09-1",
                    end: "2018-09-2"
                },
                {
                    title: "Marketing trip",
                    start: "2018-09-6",
                    end: "2018-09-8"
                },
                {
                    title: "Follow up",
                    start: "2018-10-12"
                },
                {
                    title: "Team",
                    start: "2018-10-17"
                },
                {
                    title: "Company Trip",
                    start: "2018-10-25",
                    end: "2018-10-27"
                },
                {
                    title: "Review",
                    start: "2018-11-12"
                },
                {
                    title: "Plan",
                    start: "2018-11-18"
                }
            ],
            eventColor: "rgba(54, 162, 235, 0.4)"
        });
    }
}
