function one(){$.post('http://192.168.10.123:9001/session_test',function (data) {
    // console.log('+++++++++++++++++++++++'+data)
      var userid = data.data.userid;
      document.getElementById('msg').innerHTML=userid
    })}
    function add(){
    var _html;
    var __html;
         _html = '<tr> <th>key:<input class="key" type="text" value=""></th><th>value:<input class="value" type="text"value=""></th>' +
            '<th><button class="deletes" id="clear" onclick="deleteRow(this)">--</button></th></tr>';

         __html = '<tr><th><label class="layui-form-label body-font">key:</label><input type="text" name="title" required lay-verify="required" autocomplete="off" class="layui-input key"></th>' +
            '<th class="values"><label class="layui-form-label body-font-value">value:</label><input type="text" name="title" required lay-verify="required" autocomplete="off" class="layui-input value"></th>' +
             '<th><button type="button" class="layui-btn layui-btn-sm delete" id="clear" onclick="deleteRow(this)"><i class="layui-icon">&#xe640;</i></button></th> </tr>';
        $("#table").append(__html);
    }
            // '<tr><th><label class="layui-form-label body-font">key:</label><input type="text" name="title" required lay-verify="required" autocomplete="off" class="layui-input key"></th>' +
            // '<th class="values"><label class="layui-form-label body-font-value">value:</label><input type="text" name="title" required lay-verify="required" autocomplete="off" class="layui-input value"></th>' +
            //  '<th><button type="button" class="layui-btn layui-btn-sm add" id="add" onclick="add()"><i class="layui-icon">&#xe654;</i></button></th>' +
            //  '<th><button type="button" class="layui-btn layui-btn-sm delete" id="clear" onclick="deleteRow(this)"><i class="layui-icon">&#xe640;</i></button></th> </tr>';
    function add_header(){
        var html = '<tr> <th>key:<input class="key-header" type="text" value=""></th><th>value:<input class="value-header" type="text"value=""></th>' +
            '<th><button class="deletes" id="clear" onclick="deleteRow2(this)">--</button></th></tr>';
        $("#table-header").append(html);
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
        var _html = ''
        $.post('http://192.168.10.123:9001/UserHistory' , function (data) {
        json_data = JSON.parse(data);
        // console.log(json_data.data);
        for(var i=json_data.data.length-1;i>=0;i--){
            // console.log(i,json_data.data)
            _html += '<tr><a href="#" onclick="getBody('+i+')">'+json_data.data[i].host+'</a><br/>'+json_data.data[i].create_date+'<br/>'+"接口名称:"+json_data.data[i].CaseName+'<button onclick="deletecase('+i+')">删除</button></tr>'
        }
        $("#historys").html(_html)
    })}
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
        var CaseName = $('#CaseName').val();
        if ($('input[name="name1"]:checked').val() == 'post') {
            var postdata = [];
            var postheader = [];
            var key = $('.key');
            var value = $('.value');
            var header_key = $('.key-header');
            var header_value = $('.value-header');
            if (typeof (key) == 'object' && typeof (value) == 'object') {
                for (var i = 0; i < key.length; i++) {
                    if (isNull(key[i].value)) {
                        chkstrlen(key[i].value);
                        var mn = key[i].value + '--' + value[i].value;
                        postdata.push(mn);
                    }
                }
            }
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
            var req = {
                url: url,
                data: JSON.stringify(postdata),
                header: JSON.stringify(postheader),
                type: 'post',
                CaseName: CaseName
            };
            $.post('http://192.168.10.123:9001/reqJson', req, function (data) {
                var json_response = JSON.parse(data);
                if(json_response.msg=='登录超时'){
                    alert('登录过期，请重新登录')
                }
                userhistory();
                var str_rep = formatJson(json_response.data)
                document.getElementById('response_text').innerHTML = '<pre>' + str_rep + '<pre/>';
            });
        } else {
            var postdata = [];
            var key = $('.key');
            var value = $('.value');
            if (typeof (key) == 'object' && typeof (value) == 'object') {
                for (var i = 0; i < key.length; i++) {
                    var mn = key[i].value + '--' + value[i].value;
                    postdata.push(mn);
                }
                var req = {url: url, data: postdata, type: 'get', CaseName: CaseName};
                $.post('http://192.168.10.123:9001/reqJson', req, function (data) {
                    userhistory();
                    var json_response = JSON.parse(data);
                    var str_rep = formatJson(json_response.data)
                    document.getElementById('response_text').innerHTML = '<pre>' + str_rep + '<pre/>';
                });
            } else {
                $.post('http://192.168.10.123:9001/reqJson', {
                    url: url,
                    key: key,
                    value: value,
                    type: 'get',
                    CaseName: CaseName
                }, function (data) {
                    userhistory();
                    var json_response = JSON.parse(data);
                    var str_rep = formatJson(json_response.data)
                    document.getElementById('response_text').innerHTML = '<pre>' + str_rep + '<pre/>';
                })
            }
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
            alert('参数key不允许输入汉字')
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
