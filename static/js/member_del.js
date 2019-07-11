$(function() {
    $.post('http://192.168.10.123:9001/userDelList',function(data){
        json_data = JSON.parse(data)
        var _html,sex,status,num = ''
        num = 0
        for(var i=json_data.data.length-1;i>=0;i--){
            num ++
            if(json_data.data[i].sex == 1){
                sex = '男'
            }else {
                sex = '女'
            }
             _html += '<tr><td>'+num+'</td><td>'+json_data.data[i].username+'</td><td>'+sex+'</td>';
             _html += '<td>'+json_data.data[i].create_time+'</td><td class="td-status"><span class="layui-btn layui-btn-danger layui-btn-mini">已删除</span>'
            _html += '<td class="td-manage"><a title="恢复" onclick="member_recover(this,'+i+')" href="javascript:;"><i class="layui-icon">&#xe669;</i></a></td>'
        }
        $("#delCustomerList").html(_html)
    }
    )
})