
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
            location.reload()
        }
     ,success: function(layero){
    }

});
}

        function gradeChange(r){
                var cp = document.getElementById("pid-cp");
                var grade = cp.options[cp.selectedIndex].grade;

                // var mk = document.getElementById("pid-mk");
                // var grade = mk.options[mk.selectedIndex].grade;
            // }


        alert(grade);
       }