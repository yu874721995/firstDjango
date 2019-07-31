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
                    '<th style="width:30%"><i>key:</i><input class=\'key-header\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    '<th style="width:30%"><i>value:</i><input class=\'value-header\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
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
        var _html = '';
        var search = $('#input-find').val();
        $.post('http://192.168.10.123:9001/UserHistory' ,{search:search},function (data) {
            json_data = JSON.parse(data);
            for(var i=json_data.data.length-1;i>=0;i--){
                //此处必须用div包裹，否则无法渲染！
                _html += '<div><a href="#" style="text-decoration: underline;color: orange" onclick="getBody('+i+')">'+json_data.data[i].host+'</a><br/>'+json_data.data[i].create_date+'<br/>'+"接口名称:"+json_data.data[i].CaseName+'<button class="layui-btn layui-btn-sm" onclick="deleteHistory('+i+')">删除</button><hr/></div>'
            }

            $("#historys").html(_html)
    })};

    function deleteHistory(r) {
    req = {caseId:json_data.data[r].id};
        $.post('http://192.168.10.123:9001/deleteHistory' , req,function (data) {
            userhistory()
        })
    }
    function getBody(intstt) {
        $('#response_text').val(  '')
        $('#request-bodys').val('')
        $('#request-headers').val('')
        $('#table').html('<tr style="height: 40px;">\n' +
                    '<th style="width:30%">key:<input class=\'key\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    ' <th style="width:30%">value:<input class=\'value\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    '<th style="width:5%"><button type="button" class="layui-btn layui-btn-sm deletes" id="clear" onclick="deleteRow(this)"><i class="layui-icon">&#xe640;</i></button></th>' +
                    '<th><button type="button" class="layui-btn layui-btn-sm" id="add" onclick="add()"><i class="layui-icon">&#xe654;</i></button></th></tr>')
        $('#table-header').html('<tr style="height: 40px;">\n' +
                    '<th style="width:30%"><i>key:</i><input class=\'key-header\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    '<th style="width:30%"><i>value:</i><input class=\'value-header\' type="text" value="" style="width:82%;height:30px;border: 1px solid #dddddd"></th>\n' +
                    '<th style="width:5%;"><button type="button" class="layui-btn layui-btn-sm deletes" id="clear-header" onclick="deleteRow2(this)"><i class="layui-icon">&#xe640;</i></button></th>' +
                    '<th><button type="button" class="layui-btn layui-btn-sm" id="add-header" onclick="add_header()"><i class="layui-icon">&#xe654;</i></button></th></tr>')
        // console.log('------',json_data.data[intstt].host)
        document.getElementById('url').value = json_data.data[intstt].host;
        document.getElementById('caseName').value = json_data.data[intstt].CaseName;
        document.getElementById('request-bodys').value = json_data.data[intstt].json_body;
        document.getElementById('request-headers').value = json_data.data[intstt].json_header;
        var len = Object.keys(json_data.data[intstt].body);
        json_data.data[intstt].type == 'post'?$('#selected').val('2'):$('#selected').val('1')
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
            if (n == header.length){
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
            var postdata = [];
            var postheader = [];
            var CaseName = $('#caseName').val();
            var request_body = $('#request-bodys').val()
            var request_header = $('#request-headers').val()
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
        //2为post，1为get
        if ($('#selected option:selected').val() == '2') {

            var req;

            //不能同时传值类型参数和json格式数据
            if(request_body != '' && postdata != undefined && postdata != [] &&  postdata != ''){
                layer.msg('不能同时使用两种参数')
                return false
            }
            if(request_header != '' && postheader != undefined && postheader != [] && postdata != ''){
                layer.msg('不能同时使用两种头部参数')
                return false
            }
            req = {
                url:url,
                data:JSON.stringify(postdata),
                header:JSON.stringify(postheader),
                type:'post',
                CaseName:CaseName,
                json_data:request_body,
                json_header:request_header
            }
            //发送异步请求
            $.post('http://192.168.10.123:9001/reqJson', req, function (data) {
                var json_response = JSON.parse(data);
                if(json_response.msg=='登录超时'){
                    layer.msg('登录过期，请重新登录')
                    return false
                }
                if(json_response.status != 1) {
                    layer.msg(json_response.msg)
                }else {
                    layer.msg('操作成功')
                }
                userhistory();
                var str_rep = formatJson(json_response.data)
                document.getElementById('response_text').innerHTML = '<pre>' + str_rep + '<pre/>';
            });

        //    如果为get请求时-----
        } else {
            var get_req;
            console.log('------>',request_body,'------>',postdata,)
            if(request_body != '' || postdata != '' && postdata != []){
                layer.msg('请求方式为get时请直接将参数拼接在url后')
                return false
            }
            get_req = {
                url:url,
                type:'get',
                CaseName:CaseName,
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

function openAdd(){
            var url = $('#url').val();
            var CaseName = $('#caseName').val();
            var request_body = $('#request-bodys').val();
            var request_header = $('#request-headers').val();
            var key = $('.key');
            var value = $('.value');
            var header_key = $('.key-header');
            var header_value = $('.value-header');
            var types = $('#selected option:selected').val()
            var postdata = [];
            var postheader = [];
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
            if(request_body != '' && postdata != undefined && postdata != [] &&  postdata != ''){
                layer.msg('不能同时使用两种参数')
                return false
            }
            if(request_header != '' && postheader != undefined && postheader != [] && postdata != ''){
                layer.msg('不能同时使用两种头部参数')
                return false
            }
        parent.layer.open({
        type:2
        ,title: '添加用例'
        ,content:'./static/caseupdate.html'
        ,skin:'layui-layer-lan'
        ,area: ['1000px', '600px']
        ,btnAlign: 'c'
        ,maxmin: true
        ,shadeClose:true
         ,success: function(layero,index){
              var body = parent.layer.getChildFrame('body', index);
              body.find('#casename').val(CaseName);
              body.find('#caseurl').val(url);
              postdata == '' ?body.find('#bodyText').val(request_body) : body.find('#bodyText').val(JSON.stringify(postdata));
              postheader == '' ?body.find('#headerText').val(request_header) : body.find('#headerText').val(JSON.stringify(postheader))
              $.post('http://192.168.10.123:9001/queryForProduct',{},function (data) {
                  var _html,json_data;
                  json_data = JSON.parse(data).data
                  for (var i = 0; i < json_data.length; i++) {
                            _html += "<option value='"+json_data[i].id+"'>"+json_data[i].name+"</option>"
                        }
                        body.find('#pid-cp').append(_html);
              })
        }
        ,end:function(data){
            window.location.reload()
            }
})}

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
