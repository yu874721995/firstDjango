
$(function() {
    $.post('http://192.168.10.123:9001/userList',function (data) {
                      console.log(data)

        }
    );
    $.post('http://192.168.10.123:9001/userList',function(data){
        json_data = JSON.parse(data)
        _html = ''
        sex = ''
        for(var i=json_data.data.length-1;i>=0;i--){
            if(json_data.data[i].sex == 1){
                sex = '男'
            }else {
                sex = '女'
            }
            console.log(json_data.data)
            _html += '<tr><td><input type="checkbox" name="id" value="3"  lay-skin="primary">';
             _html += '</td><td>'+json_data.data[i].id+'</td><td>'+json_data.data[i].username+'</td><td>'+sex+'</td>';
             _html += '<td>'+json_data.data[i].old_login_time+'</td>'
             _html += '<td class="td-status"><span class="layui-btn layui-btn-normal layui-btn-mini">已启用</span></td>';
             _html += '<td class="td-manage"><a onclick="member_stop(this,\'10001\')" href="javascript:;"  title="启用">';
             _html += '<i class="layui-icon">&#xe601;</i></a><a title="编辑"  onclick="xadmin.open(\'编辑\',\'member-edit.html\',600,400)" href="javascript:;">';
            _html += '<i class="layui-icon">&#xe642;</i></a>'
            _html += '<a onclick="xadmin.open("修改密码","/static/member-password.html",600,400)" title="修改密码" href="javascript:;">';
            _html += '<i class="layui-icon">&#xe631;</i></a><a title="删除" onclick="member_del(this,"要删除的id")" href="javascript:;">';
            _html += '<i class="layui-icon">&#xe640;</i></a></td></tr>'

        }
        $("#customerList").html(_html)
    }
    )
})