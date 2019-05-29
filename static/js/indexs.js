function one(){$.post('http://192.168.10.123:9001/session_test',function (data) {
    console.log('+++++++++++++++++++++++'+data)
      var userid = data.data.userid;
      document.getElementById('msg').innerHTML=userid
    })}

    function add(){
        var html = '<tr> <th>key:<input class="key" type="text" value=""></th><th>value:<input class="value" type="text"value=""></th>' +
            '<th><button class="deletes" id="clear" onclick="deleteRow(this)">--</button></th></tr>';
        $("#table").append(html);
    }
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
        $.post('http://192.168.10.123:9001/user' , function (data) {
        var json_data = JSON.parse(data);
        var username = json_data.data.username;
        document.getElementById('msg').innerHTML = username;
})
}

    function userhistory() {
        var _html = ''
        $.post('http://192.168.10.123:9001/UserHistory' , function (data) {
        json_data = JSON.parse(data);
        console.log(json_data.data);
        for(var i=json_data.data.length-1;i>=0;i--){
            console.log(i,json_data.data)
            _html += '<tr><a href="#" onclick="getBody('+i+')">'+json_data.data[i].host+'</a><br/>'+json_data.data[i].create_date+'<br/>'+"接口名称:"+json_data.data[i].CaseName+'</tr>'
        }
        $("#historys").html(_html)
    })}

    function getBody(intstt) {
        $('#table').html('<tr> <th>key:<input class="key" type="text" value=""></th><th>value:<input class="value" type="text"value=""></th>' +
            '<th><button class="deletes" id="clear" onclick="deleteRow(this)">--</button></th></tr>'+'<th><button id="add" onclick="add()">添加参数</button></th>')
        console.log('------',json_data.data[intstt].host)
        document.getElementById('url').value = json_data.data[intstt].host;
        document.getElementById('CaseName').value = json_data.data[intstt].CaseName;
        var len = Object.keys(json_data.data[intstt].body);
        var s = 0;
        for(var i in json_data.data[intstt].body)
        {
            console.log('~~~~~~~~~~~~~',i);
            document.getElementsByClassName('key')[s].value += i;
            console.log('@@@@@@@@@@@',json_data.data[intstt].body[i]);
            document.getElementsByClassName('value')[s].value += json_data.data[intstt].body[i];
            s ++
            if (s == len.length){
                break
            }
            add();
        }
        r_body = json_data.data[intstt].response_body
        console.log(r_body)
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

    function reqJson() {
        var url = $('#url').val();
        var CaseName = $('#CaseName').val();
        if($('input[name="name1"]:checked').val() == 'post'){
            var postdata = [];
            var postheader = [];
            var key = $('.key');
            var value = $('.value');
            var header_key = $('.key-header');
            var header_value = $('.value-header');
            console.log('-----1---1--1-1-1--1-1-1--1-1-1--1--1',header_key,header_value);
            if(typeof(key)=='object' && typeof(value)=='object'){
                for(var i=0;i<key.length;i++){
                    var mn =key[i].value +':'+value[i].value;
                    postdata.push(mn);
                }
                console.log(JSON.stringify(postdata))
                var req = {url:url,data:postdata,type:'post',CaseName:CaseName};
                $.post('http://192.168.10.123:9001/reqJson', req , function (data){
                    userhistory();
                    var json_response = JSON.parse(data);
                    var str_rep = formatJson(json_response.data)
                    document.getElementById('response_text').innerHTML='<pre>'+str_rep+'<pre/>';
                });
            }else{
                $.post('http://192.168.10.123:9001/reqJson', {url:url,key:key,value:value,type:'post',CaseName:CaseName}, function (data){
                     userhistory();
                   var json_response = JSON.parse(data);
                    var str_rep = formatJson(json_response.data)
                    document.getElementById('response_text').innerHTML='<pre>'+str_rep+'<pre/>';
                })
            }
        }else{
            var postdata = [];
            var key = $('.key');
            var value = $('.value');
            if(typeof(key)=='object' && typeof(value)=='object'){
                for(var i=0;i<key.length;i++){
                    var mn =key[i].value +':'+value[i].value;
                    postdata.push(mn);
                }
                console.log(JSON.stringify(postdata))
                var req = {url:url,data:postdata,type:'get',CaseName:CaseName};
                $.post('http://192.168.10.123:9001/reqJson', req , function (data){
                     userhistory();
                    var json_response = JSON.parse(data);
                    var str_rep = formatJson(json_response.data)
                    document.getElementById('response_text').innerHTML='<pre>'+str_rep+'<pre/>';
                });
            }else{
                $.post('http://192.168.10.123:9001/reqJson', {url:url,key:key,value:value,type:'get',CaseName:CaseName}, function (data){
                     userhistory();
                   var json_response = JSON.parse(data);
                    var str_rep = formatJson(json_response.data)
                    document.getElementById('response_text').innerHTML='<pre>'+str_rep+'<pre/>';
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
                    var mn =key[i].value +':'+value[i].value;
                    postdata.push(mn);
                }
                console.log(JSON.stringify(postdata))
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
                    var mn =key[i].value +':'+value[i].value;
                    postdata.push(mn);
                }
                console.log(JSON.stringify(postdata))
                var req = {url:url,data:postdata,type:'get'};
                $.post('http://192.168.10.123:9001/SaveTestCase', req , function (data){

                });
            }else{
                $.post('http://192.168.10.123:9001/SaveTestCase', {url:url,key:key,value:value,type:'get'}, function (data){

                })
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
        console.log(typeof json)
        if (typeof json !== 'string') {
            console.log(typeof json)
            json = JSON.stringify(json);
         } else {
            try{
                console.log(typeof json);
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
