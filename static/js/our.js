
function addcpChoice(name) {
    var repjson;
    if(name == 'cp'){
        //打开添加产品弹窗
        parent.layer.prompt({
              value: '',
              title: '请输入产品名称',
              area: ['800px', '350px'] //自定义文本域宽高
            }, function(value, index, elem){
                 $.post('http://192.168.10.123:9001/addChoice',{cpname:value,type:1},function(data){
                    repjson = JSON.parse(data)
                    if(repjson.status == 1){
                        parent.layer.close(index);
                    }else {
                        parent.layer.msg(repjson.msg)
                    }
                })

            });
    }else {
            //打开添加模块弹窗
            parent.layer.open({
                type: 1
                , title: '添加模块'
                , content: '<div class="layui-form" style="margin: 30px">' +
                    '<form class="layui-form" action="">' +
                    '<div class="layui-form-item">\n' +
                    '<label class="layui-form-label">产品名称</label>' +
                    '<div class="layui-inline"><select class="layui-select" style="width: 190px;display: inline-block!important;" id="cp" lay-verify="required" name="cpChoice" lay-search></select></div>' +
                    '<div class="layui-inline"><button type="button" onclick="addcpChoice(\'cp\')" class="layui-btn layui-btn-sm"><i class="layui-icon">&#xe654;</i></button></div></div>' +
                    '<div class="layui-form-item" id="name-mk" style="margin-top: 50px"><label class="layui-form-label">模块名称</label>' +
                    '<input id="mkName" type="text" name="mkName" required lay-verify="required" placeholder="请输入模块名称" autocomplete="off" class="layui-input layui-input-inline"></div>' +
                    '</form></div>'
                // '<div class="layui-form-item"><div class="layui-input-block"><button class="layui-btn" lay-submit lay-filter="choiceDemo">添加</button></div></div>'
                , skin: 'layui-layer-lan'
                , area: ['500px', '400px']
                , btn: '添加'
                , btnAlign: 'c'
                , shadeClose: true
                //异步发送添加模块请求
                , yes: function (index, layero) {
                    //点击确认按钮时的操作回调
                    var repjson,cpname;
                    var cpname = layero.find('#mkName').val()
                    var subjection = layero.find('#cp option:selected').val()
                    $.post('http://192.168.10.123:9001/addChoice', {cpname: cpname,subjection:subjection,type: 2}, function (data) {
                        repjson = JSON.parse(data)
                        if (repjson.status == 1) {
                            parent.layer.close(index);
                        } else {
                            parent.layer.msg(repjson.msg)
                        }
                    })
                }
                //打开添加页面是读取产品列表
                , success: function (layero) {
                    $.post('http://192.168.10.123:9001/queryForProduct', {}, function (data) {
                        var pro;
                        var _html;
                        var pro = JSON.parse(data).data;
                        console.log(data);
                        for (var i = 0; i < pro.length; i++) {
                            _html += "<option value='"+pro[i].id+"'>"+pro[i].name+"</option>"
                        }
                        layero.find('#cp').html(_html);
                                })
                }
            })
    }};




