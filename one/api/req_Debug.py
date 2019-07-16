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
        posturl = request.POST.get('url', None)
        geturl = posturl + '?'
        body = request.POST.getlist('data', None)
        header = request.POST.getlist('header', None)
        token = request.POST.get('token', None)
        CaseName = request.POST.get('CaseName', None)
        headers = {}
        user_id = request.session.get('user_id', None)
        types = request.POST.get('type', None)
        data = {}

        if user_id is None or user_id == '1':
            return HttpResponse(json.dumps({'status': 200, 'msg': '登录超时'}))

        if not token is None:
            login_token = self.findToken(user_id)
            if not login_token:
                return HttpResponse(json.dumps({'status': 5, 'msg': '没有找到token或token已失效'}))
            headers['Authorization'] = login_token
        else:
            pass

        #如果使用的是json格式字符串
        try:
            if len(body[0].split('--')) == 1:
                data = eval(body[0])
            else:
                # 处理传入的body
                body = json.loads(body[0])
                for i in body:
                    data[i.split('--')[0]] = i.split('--')[1]
                    geturl += i.split('--')[0] + '=' + i.split('--')[1]
        except Exception as e:
            print('error--------------',e)
            return  HttpResponse(json.dumps({'status': 500, 'msg': '请检查提交的参数格式'}))

        #同上，处理headers
        try:

            if len(header[0].split('--')) == 1:
                headers = eval(header[0])
            else:
                # 处理传入的headers
                header = json.loads(header[0])
                for i in header:
                    headers[i.split('--')[0]] = i.split('--')[1]
        except Exception as e:
            print('error--------------', e)
            return HttpResponse(json.dumps({'status': 500, 'msg': '请检查提交的header格式'}))

        resopnse_body = ''
        # 发送请求
        print('发送请求的参数:', 'url:', posturl, 'data：', data, 'header:', headers)
        if types == 'post':
            try:
                r = requests.post(posturl, data=data, headers=headers)
                resopnse_body = r.json()
            except Exception as e:
                print('error--------------', e)
                return HttpResponse(json.dumps({'status': 2, 'msg': '请求错误'}))
        elif types == 'get':
            try:
                r = requests.get(geturl)
                resopnse_body = r.json()
            except Exception as e:
                return HttpResponse(json.dumps({'status': 2, 'msg': '请求错误'}))
        # 存入历史
        try:
            dic = {'host': posturl, 'userid': user_id, 'response_body': resopnse_body, 'method': types,
                   'casename': CaseName}
            models.user_host.objects.create(**dic)

            host = models.user_host.objects.filter(host=posturl).order_by('-create_date')
            host_id = host.values()[0]['id']
            # 存入body
            for i in body:
                dic = {'key': i.split('--')[0], 'value': i.split('--')[1], 'host_id_id': host_id, 'type': 1}
                models.user_body.objects.create(**dic)
            # 存入header
            for i in header:
                dic = {'key': i.split('--')[0], 'value': i.split('--')[1], 'host_id_id': host_id, 'type': 2}
                models.user_body.objects.create(**dic)
        except Exception as e:
            return HttpResponse(json.dumps({'status': 1, 'msg': e, }))
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



