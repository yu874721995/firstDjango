
$(function() {
    $.post('http://192.168.10.123:9001/session_test',function (data) {
                      console.log(data)
                      var s = JSON.parse(data).data.username;
                      var time = JSON.parse(data).data.time
                      $("#customerName").text(s);
                      $('#nowtime').text(time)
        }
    );
})