
function addProducts(name) {
    parent.layer.open({
        type:1
    ,title: '添加' + name
    ,content: '<div class="layui-input-inline">\n' +
            '            <input type="password" name="password" required lay-verify="required" placeholder="请输入断言内容" autocomplete="off" class="layui-input">\n' +
            '          </div>'
     ,skin:'layui-layer-lan'
     ,area: ['400', '300px']
     ,btn :'添加'
     ,btnAlign: 'c'
     ,shadeClose:true
     ,yes: function(index, layero) {
            //do something
            layer.close(index);
        }
     ,success: function(layero){
    }

});
}

function submit() {
    alert('jjjjjjjjj')
}

function gradeChange(r){
                var cp = document.getElementById("pid-cp");
                var grade = cp.options[cp.selectedIndex].grade;

                // var mk = document.getElementById("pid-mk");
                // var grade = mk.options[mk.selectedIndex].grade;
            // }


        alert(grade);
       }

function addcpChoice(name) {
    var repjson;
    if(name == 'cp'){
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
        //     parent.layer.open({
//         type:1
//     ,title: '添加产品'
//     ,content:'<form class="layui-form" action=""><div class="layui-form-item" style="margin-top: 50px"><label class="layui-form-label">产品名称</label>' +
//             '<input id="cpName" type="text" name="cpName" required lay-verify="required" placeholder="请输入产品名称" autocomplete="off" class="layui-input layui-input-inline"></div></form>'
//             // '<div class="layui-form-item"><div class="layui-input-block"><button class="layui-btn" lay-submit lay-filter="choiceDemo">添加</button></div></div>'
//      ,skin:'layui-layer-lan'
//      ,area: ['400px', '300px']
//      ,btn :'添加'
//      ,btnAlign: 'c'
//      ,shadeClose:true
//      ,yes: function(index, layero) {
//             // //点击确认按钮时的操作回调
//             // var repjson,cpname;
//             // var hh = parent.layer.getChildFrame('form',layer.index);
//             // console.log(hh)
//             // var cpname = $('#cpName').val()
//             // console.log('cpname',cpname)
//             // $.post('http://192.168.10.123:9001/addChoice',{cpname:cpname,type:1},function(data){
//             //     repjson = JSON.parse(data)
//             //     if(repjson.status == 1){
//             //         parent.layer.
//             //         parent.layer.close(index);
//             //     }else {
//             //         parent.layer.msg(repjson.msg)
//             //     }
//             // })
//             // location.reload()
//
//         }
//      ,success: function(layero){
//     }
// })
    }};