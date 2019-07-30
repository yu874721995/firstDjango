#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/7/10 20:54
@Author  : Careslten
@Site    : 
@File    : req_Debug.py
@Software: PyCharm
'''

from django.http import HttpResponse
from one import models
import json
import requests

class req_debug():

    # 处理请求
    def reqJson(self,request):
        print('request_body', request.POST)
        url = request.POST.get('url', None) #host
        body = request.POST.getlist('data', None)#参数列表
        header = request.POST.getlist('header', None)#请求头
        CaseName = request.POST.get('CaseName', None)#接口名称
        user_id = request.session.get('user_id', None)
        types = request.POST.get('type', None)#请求方式
        json_data = request.POST.get('json_data','')
        json_header = request.POST.get('json_header','')

        data = {}
        headers = {}
        resopnse_body = ''

        if user_id is None or user_id == '1':
            return HttpResponse(json.dumps({'status': 200, 'msg': '登录超时'}))
        if types == 'post':
            #如果使用的是json格式字符串
            try:
                if json_data != '' and json_data != None:
                    data = eval(json_data)
                else:
                    # 处理传入的body
                    body = json.loads(body[0])
                    for i in body:
                        data[i.split('--')[0]] = i.split('--')[1]
            except Exception as e:
                print('error--------------1',e)
                return  HttpResponse(json.dumps({'status': 500, 'msg': '请检查提交的参数格式'}))

            #同上，处理headers
            try:
                if json_header != '' and json_header != None:
                    headers = eval(json_header)
                else:
                    # 处理传入的headers
                    header = json.loads(header[0])
                    for i in header:
                        headers[i.split('--')[0]] = i.split('--')[1]
            except Exception as e:
                print('error--------------2', e)
                return HttpResponse(json.dumps({'status': 500, 'msg': '请检查提交的header格式'}))
            print('hhhh', url, body, header, CaseName, user_id, types, json_data, json_header,headers,data)
            # 发送请求
            print('发送post请求的参数:', 'url:', url, 'data：', data, 'header:', headers)

            try:
                r = requests.post(url, data=data, headers=headers)
                print(r.text)
                resopnse_body = r.json()

            except Exception as e:

                print('error--------------3', e)
                return HttpResponse(json.dumps({'status': 500, 'msg': '请求错误'}))

            # 存入历史
            try:
                if user_id == 16 or user_id == '16':
                    return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data': resopnse_body}))

                dic = {'host': url, 'userid': user_id, 'response_body': resopnse_body, 'method': types,'json_body':json_data,'json_header':json_header,
                       'casename': CaseName}
                models.user_host.objects.create(**dic)
                host = models.user_host.objects.filter(host=url).order_by('-create_date')
                host_id = host.values()[0]['id']
                print('存入host------------------------OK')

                if body != [] and json_data == '':
                    # 存入body
                    for i in body:
                        dic = {'key': i.split('--')[0], 'value': i.split('--')[1], 'host_id_id': host_id, 'type': 1}
                        models.user_body.objects.create(**dic)
                    print('存入body------------------------OK')

                if header != [] and json_header == '':
                    # 存入header
                    for i in header:
                        dic = {'key': i.split('--')[0], 'value': i.split('--')[1], 'host_id_id': host_id, 'type': 2}
                        models.user_body.objects.create(**dic)
                    print('存入header------------------------OK')
            except Exception as e:
                print('error----------------4',e)
                return HttpResponse(json.dumps({'status': 500, 'msg': '请求错误' }))
            return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data': resopnse_body}))
        #处理get请求
        else:
            try:
                print('get请求---------------网址：',url)
                r = requests.get(url)
                try:
                    resopnse_body = r.json()
                except Exception as e:
                    print(r.text)
                    resopnse_body = r.text
            except Exception as e:
                print('error--------------5', e)
                return HttpResponse(json.dumps({'status': 500, 'msg': '请求错误'}))
            try:
                dic = {'host': url, 'userid': user_id, 'response_body': resopnse_body, 'method': types,
                       'casename': CaseName}
                models.user_host.objects.create(**dic)
            except Exception as e:
                print('error--------------6',e)
                return HttpResponse(json.dumps({'status': 500, 'msg': '请求错误'}))
            return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data': resopnse_body}))


    def findToken(self,user_id):
        token_body = models.user_host.objects.filter(user_id=user_id).order_by('-create_date')
        for i in token_body:
            try:
                if i[3]['token']:
                    token = 'Bearer ' + i[3]['token']
                    return token
            except:
                return False



