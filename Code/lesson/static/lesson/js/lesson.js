$(function() {
    var initChart = function() {
        var ctx_average = $("#chart-average").get(0).getContext("2d");
        window.myLine = new Chart(ctx_average).Line(lineChartData);
        var ctx_distribution = $("#chart-distribution").get(0).getContext("2d");
        window.myPie = new Chart(ctx_distribution).Pie(pieData);
    }
    initChart();

    $('#comment-iframe').load(function() {
        var data = JSON.parse($('#comment-iframe').contents().find('body').html());
        alert(data['result']);
    });

    $('#file-upload-iframe').load(function() {
        var data = JSON.parse($('#file-upload-iframe').contents().find('body').html());
        alert(data['result']);
    });
});
