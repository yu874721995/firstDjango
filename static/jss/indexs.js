function one(){$.post('http://192.168.10.123:9001/session_test',function (data) {
    // console.log('+++++++++++++++++++++++'+data)
      var userid = data.data.userid;
      document.getElementById('msg').innerHTML=userid
    })}
    function add(){
    var __html;
         __html += '<tr style="height: 40px;">\n' +
                    '<th style="width:30%">key:<input class=\'key\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    ' <th style="width:30%">value:<input class=\'value\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    '<th style="width:5%"><button type="button" class="layui-btn layui-btn-sm deletes" id="clear" onclick="deleteRow(this)"><i class="layui-icon">&#xe640;</i></button></th></tr>'
        $("#table").append(__html);
    }

    function add_header(){
        var __html;
         __html += '<tr style="height: 40px;">\n' +
                    '<th style="width:30%"><i>key:</i><input class=\'key\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    '<th style="width:30%"><i>value:</i><input class=\'value\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    '<th style="width:5%;"><button type="button" class="layui-btn layui-btn-sm deletes" id="clear-header" onclick="deleteRow2(this)"><i class="layui-icon">&#xe640;</i></button></th></tr>'
        $("#table-header").append(__html);
    }
    //请求用户名
(function(){
        userhistory(),username();
})()

function username() {
        $.post('http://192.168.10.123:9001/username' , function (data) {
        var json_data = JSON.parse(data);
        var username = json_data.data.username;
        $('#customerName').text(username);
})
}
    function userhistory() {
    // var table = layui.table;
    //         table.render({
    //       elem: '#historys' //指定原始表格元素选择器（推荐id选择器）
    //       ,height: 315 //容器高度
    //       ,cols:[[ //表头
    //   {field: 'id', title: 'ID', width:80, sort: true, fixed: 'left'}
    // ]] //设置表头
    //       ,url:'http://192.168.10.123:9001/UserHistory'
    //       ,method:'post'
    //       ,request:{search:''}
    //       ,done:function (res) {
    //                 console.log(res)
    //
    //             }
    //     });
        var _html = '';
        var search = $('#input-find').val();
        $.post('http://192.168.10.123:9001/UserHistory' ,{search:search},function (data) {
            json_data = JSON.parse(data);
            for(var i=json_data.data.length-1;i>=0;i--){
                //此处必须用div包裹，否则无法渲染！
                _html += '<div><a href="#" style="text-decoration: underline;color: orange" onclick="getBody('+i+')">'+json_data.data[i].host+'</a><br/>'+json_data.data[i].create_date+'<br/>'+"接口名称:"+json_data.data[i].CaseName+'<button class="layui-btn layui-btn-sm" onclick="deletecase('+i+')">删除</button><hr/></div>'
            }

            $("#historys").html(_html)
    })};

    function deletecase(r) {
    req = {caseId:json_data.data[r].id};
        $.post('http://192.168.10.123:9001/deletecase' , req,function (data) {
            userhistory()
        })
    }
    function getBody(intstt) {
        $('#table').html('<tr> <th>key:<input class="key" type="text" value=""></th><th>value:<input class="value" type="text"value=""></th>' +
            '<th><button class="deletes" id="clear" onclick="deleteRow(this)">--</button></th></tr>'+'<th><button id="add" onclick="add()">添加参数</button></th>')
        $('#table-header').html('<tr> <th>key:<input class="key-header" type="text" value=""></th><th>value:<input class="value-header" type="text"value=""></th>' +
            '<th><button class="deletes" id="clear" onclick="deleteRow2(this)">--</button></th></tr>'+'<th><button id="add" onclick="add_header()">添加参数</button></th>')
        // console.log('------',json_data.data[intstt].host)
        document.getElementById('url').value = json_data.data[intstt].host;
        document.getElementById('CaseName').value = json_data.data[intstt].CaseName;
        var len = Object.keys(json_data.data[intstt].body);
        var header = Object.keys(json_data.data[intstt].header);
        var s = 0;
        var n = 0;
        for(var i in json_data.data[intstt].body)
        {
            document.getElementsByClassName('key')[s].value += i;
            document.getElementsByClassName('value')[s].value += json_data.data[intstt].body[i];
            s ++
            if (s == len.length){
                break
            }
            add();
        }
        for(var s in json_data.data[intstt].header){
            document.getElementsByClassName('key-header')[n].value += i;
            document.getElementsByClassName('value-header')[n].value += json_data.data[intstt].header[s];
            n ++
            if (n == len.length){
                break
            }
            add();
        }
        r_body = json_data.data[intstt].response_body
        var response_bodys = formatJson(r_body)
        document.getElementById('response_text').innerHTML = '<pre style="word-break:break-all;display:inline-block;">'+response_bodys+'<pre/>';
    }

    function deleteRow(r) {
        var i = r.parentNode.parentNode.rowIndex;
        if(i>0) {
            document.getElementById('table').deleteRow(i)
        }
    }
    function deleteRow2(r) {
        var i = r.parentNode.parentNode.rowIndex;
        if (i > 0) {
            document.getElementById('table-header').deleteRow(i)
        }
    }
        // #发送请求
    function reqJson() {
            var url = $('#url').val();
            if(url == ''){
                layer.msg('亲,url不能为空')
                return false
            }

        var CaseName = $('#caseName').val();

        //2为post，1为get
        if ($('#selected option:selected').val() == '2') {
            var request_body = $('#request-bodys').val()
            var request_headers = $('#request-headers').val()
            var req;
            var postdata = [];
            var postheader = [];
            var key = $('.key');
            var value = $('.value');
            var header_key = $('.key-header');
            var header_value = $('.value-header');

            //处理body的key、value内容
            if (typeof (key) == 'object' && typeof (value) == 'object') {
                for (var i = 0; i < key.length; i++) {
                    if (isNull(key[i].value)) {
                        chkstrlen(key[i].value);
                        var mn = key[i].value + '--' + value[i].value;
                        postdata.push(mn);
                    }
                }
            }
            //处理headers的key、value内容
            if (typeof (header_key) == 'object' && typeof (header_value) == 'object') {
                for (var s = 0; s < header_key.length; s++) {
                    console.log('-----------------------' + isNull(JSON.stringify(header_key[s].value)))
                    if (isNull(header_key[s].value)) {
                        chkstrlen(header_key[s].value);
                        var mu = header_key[s].value + '--' + header_value[s].value;
                        postheader.push(mu);
                    }
                }
            }else {
                layer.msg('前端报错了快叫大兄弟来看看')
            }

            //不能同时传值类型参数和json格式数据
            if(request_body != '' && postdata != undefined){
                layer.msg('不能同时使用两种参数')
                return false
            }
            if(request_headers != '' && postheader != undefined){
                layer.msg('不能同时使用两种头部参数')
                return false
            }

            //如果填入了json格式字符串
            if(request_body != ''){
                if(request_headers !=''){
                    var req = {
                    url: url,
                    data: request_body,
                    header:request_headers,
                    type: 'post',
                    CaseName: CaseName}
                }else {
                    var req = {
                    url: url,
                    data: request_body,
                    header:JSON.stringify(postheader),
                    type: 'post',
                    CaseName: CaseName}
                }

            }else {
                if(request_headers !=''){
                    var req = {
                    url: url,
                    data: JSON.stringify(postdata),
                    header:request_headers,
                    type: 'post',
                    CaseName: CaseName}
                }else {
                    var req = {
                    url: url,
                    data: JSON.stringify(postdata),
                    header:JSON.stringify(postheader),
                    type: 'post',
                    CaseName: CaseName}
                }
            };
            //发送异步请求
            $.post('http://192.168.10.123:9001/reqJson', req, function (data) {
                var json_response = JSON.parse(data);
                if(json_response.msg=='登录超时'){
                    layer.msg('登录过期，请重新登录')
                    return false
                }
                userhistory();
                var str_rep = formatJson(json_response.data)
                document.getElementById('response_text').innerHTML = '<pre>' + str_rep + '<pre/>';
            });



        //    如果为get请求时-----
        } else {
            var postdata
            var get_req;
            var getheader = [];
            var header_key = $('.key-header');
            var header_value = $('.value-header');
            var get_body = $('#request-bodys').val()
            var get_headers = $('#request-headers').val()
            var CaseName = $('#caseName').val()

            //判断postdata是否为空
            if (typeof (key) == 'object' && typeof (value) == 'object') {
                for (var i = 0; i < key.length; i++) {
                    if (isNull(key[i].value)) {
                        chkstrlen(key[i].value);
                        var mn = key[i].value + '--' + value[i].value;
                        postdata.push(mn);
                    }
                }
            }
        console.log(postdata,get_body)
            if(get_body != '' || postdata != undefined ){
                layer.msg('请求方式为get时请直接将参数拼接在url后')
            }

            //处理header
            if (typeof (header_key) == 'object' && typeof (header_value) == 'object') {
                for (var s = 0; s < header_key.length; s++) {
                    console.log('-----------------------' + isNull(JSON.stringify(header_key[s].value)))
                    if (isNull(header_key[s].value)) {
                        chkstrlen(header_key[s].value);
                        var mu = header_key[s].value + '--' + header_value[s].value;
                        postheader.push(mu);
                    }
                }
            }
            // 处理header
            if(get_headers != ''){
                    get_req={
                    url: url,
                    header:get_headers,
                    type: 'get',
                    CaseName: 1}
            }else {
                get_req={
                    url: url,
                    header:JSON.stringify(postheader),
                    type: 'get',
                    CaseName: CaseName}
            }
            //发送请求
            $.post('http://192.168.10.123:9001/reqJson', get_req, function (data) {
                userhistory();
                var json_response = JSON.parse(data);
                var str_rep = formatJson(json_response.data)
                document.getElementById('response_text').innerHTML = '<pre>' + str_rep + '<pre/>';
            });
            }
    }
    function SaveTestCase(){
        var url = $('#url').val()
        var CaseName = $('#CaseName').val()
        if($('input[name="name1"]:checked').val() == 'post'){
            var postdata = [];
            var key = $('.key');
            var value = $('.value');
            if(typeof(key)=='object' && typeof(value)=='object'){
                for(var i=0;i<key.length;i++){
                    var mn =key[i].value +'--'+value[i].value;
                    postdata.push(mn);
                }
                var req = {url:url,data:postdata,type:'post',CaseName:CaseName};
                $.post('http://192.168.10.123:9001/SaveTestCase', req , function (data){

                });
            }else{
                $.post('http://192.168.10.123:9001/SaveTestCase', {url:url,key:key,value:value,type:'post'}, function (data){

                })
            }
        }else{
            var postdata = [];
            var key = $('.key');
            var value = $('.value');
            if(typeof(key)=='object' && typeof(value)=='object'){
                for(var i=0;i<key.length;i++){
                    var mn =key[i].value +'--'+value[i].value;
                    postdata.push(mn);
                }
                var req = {url:url,data:postdata,type:'get'};
                $.post('http://192.168.10.123:9001/SaveTestCase', req , function (data){

                });
            }else{
                $.post('http://192.168.10.123:9001/SaveTestCase', {url:url,key:key,value:value,type:'get'}, function (data){

                })
            }

        }
    }

//   判断是否为空
function isNull(strs) {
    if(strs == '' || strs == null || strs == "" || strs == undefined || strs.length == 0){
        return false
    }else {
        return true
    }
}

//key不允许包含中文
function chkstrlen(str) {
    for (var i = 0; i < str.length; i++) {
        if (str.charCodeAt(i) > 255) { //如果是汉字
            layer.msg('参数key不允许输入汉字')
            return
        }
    }
}




//JSON格式化
var formatJson = function (json, options) {
         var reg = null,
                 formatted = '',
                 pad = 0,
                 PADDING = '    ';
         options = options || {};
        options.newlineAfterColonIfBeforeBraceOrBracket = (options.newlineAfterColonIfBeforeBraceOrBracket === true) ? true : false;
        options.spaceAfterColon = (options.spaceAfterColon === false) ? false : true;
        // console.log(typeof json)
        if (typeof json !== 'string') {
            // console.log(typeof json)
            json = JSON.stringify(json);
         } else {
            try{
                // console.log(typeof json);
                json = JSON.parse(json);
                json = JSON.stringify(json);
            }catch (error){
             json = json;
            }
             // json = JSON.stringify(json);
         }
         reg = /([\{\}])/g;
        json = json.replace(reg, '\r\n$1\r\n');
        reg = /([\[\]])/g;         json = json.replace(reg, '\r\n$1\r\n');
         reg = /(\,)/g;
         json = json.replace(reg, '$1\r\n');
         reg = /(\r\n\r\n)/g;
         json = json.replace(reg, '\r\n');
         reg = /\r\n\,/g;
         json = json.replace(reg, ',');if (!options.newlineAfterColonIfBeforeBraceOrBracket) {reg = /\:\r\n\{/g;
         json = json.replace(reg, ':{');
         reg = /\:\r\n\[/g;
         json = json.replace(reg, ':[');
         }if (options.spaceAfterColon) {reg = /\:/g;
         json = json.replace(reg, ':');
         }
         (json.split('\r\n')).forEach(function (node, index) {
                   var i = 0,         indent = 0,
                            padding = '';

                    if (node.match(/\{$/) || node.match(/\[$/)) {
                        indent = 1;
                     } else if (node.match(/\}/) || node.match(/\]/)) {
    if (pad !== 0) {pad -= 1;
                         }
                     } else {
    indent = 0;
                     }
                   for (i = 0; i < pad; i++) {
    padding += PADDING; }
                   formatted += padding + node + '\r\n';
                   pad += indent; }
       );
       return formatted;
    };
