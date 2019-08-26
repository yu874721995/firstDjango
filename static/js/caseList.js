
function batchExecution() {
    var checkout = table.checkStatus('demo')
    var caseId = []
    if(checkout.data.length == 0){
        layer.msg('请选择用例')
        return false
    }
    for(var i=0;i<checkout.data.length;i ++){
        if(checkout.data[i].status == 0){
            layer.msg('包含已禁用的用例')
            return false
        }
        caseId.push(checkout.data[i].case_id)
    }
    console.log(caseId)
    $.post('http://192.168.10.123:9001/batchExecution',{caseId:JSON.stringify(caseId)},function (data) {
        var json_msg = JSON.parse(data).msg
        layer.msg(json_msg)

    })
}

