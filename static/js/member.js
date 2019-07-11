
$(function() {
    $.post('http://192.168.10.123:9001/userList',function(data){
        json_data = JSON.parse(data)
        var _html,sex,status,num = ''
        num = 1
        for(var i=json_data.data.length-1;i>=0;i--){

            if(json_data.data[i].sex == 1){
                sex = '男'
            }else {
                sex = '女'
            }

            status = json_data.data[i].status == 1 ? '已启用':'已停用'
             _html += '<tr><td>'+num+'</td><td>'+json_data.data[i].username+'</td><td>'+sex+'</td>';
             _html += '<td>'+json_data.data[i].old_login_time+'</td>'
            if(json_data.data[i].status == 1){
                _html += '<td class="td-status"><span class="layui-btn layui-btn-normal layui-btn-mini">'+status+'</span></td>'
                _html += '<td class="td-manage"><a onclick="member_stop(this,\'10001\','+i+')" href="javascript:;"  title="停用">'
            }else {
                _html += '<td class="td-status"><span class="layui-btn layui-btn-normal layui-btn-mini layui-btn-disabled">'+status+'</span></td>'
                _html += '<td class="td-manage"><a onclick="member_stop(this,\'10001\','+i+')" href="javascript:;"  title="启用">'
            }
             // _html += json_data.data[i].status == 1 ? '<td class="td-status"><span class="layui-btn layui-btn-normal layui-btn-mini">'+status+'</span></td>':'<td class="td-status"><span class="layui-btn layui-btn-normal layui-btn-mini layui-btn-disabled">'+status+'</span></td>'
             // _html += json_data.data[i].status == 1 ? '<td class="td-manage"><a onclick="member_stop(this,\'10001\')" href="javascript:;"  title="停用">':'<td class="td-manage"><a onclick="member_stop(this,\'10001\')" href="javascript:;"  title="启用">;
             // _html += '<i class="layui-icon">&#xe601;</i></a><a title="编辑"  onclick="xadmin.open(\'编辑\',\'member-edit.html\',600,400)" href="javascript:;">';
            // _html += '<i class="layui-icon">&#xe642;</i></a>'
            // _html += '<a onclick="xadmin.open("修改密码","/static/member-password.html",600,400)" title="修改密码" href="javascript:;">';
            _html += '<i class="layui-icon">&#xe631;</i></a><a title="删除" onclick="member_del(this,'+i+')" href="javascript:;">';
            _html += '<i class="layui-icon">&#xe640;</i></a></td></tr>'
            num ++
        }
        $("#customerList").html(_html)
    }
    )
})