(function(){
    caseList('')
})()


function caseList(r){
    if(r == '' || r == undefined){
        var req = {}
    }
    $.post('http://192.168.10.123:9001/caseList',req,function(data){
                var json_data = JSON.parse(data).data
                var json_msg = JSON.parse(data).msg
                var json_status = JSON.parse(data).status
                if(json_status == 1){
                    console.log(json_data)
                }else{
                    layer.msg(json_msg)
                }
        })
}
