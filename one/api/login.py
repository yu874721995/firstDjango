#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/7/10 21:00
@Author  : Careslten
@Site    : 
@File    : login.py
@Software: PyCharm
'''

from django.http import HttpResponse
from one import models
import json
import datetime


class Login():
    def Loginup(self,request):
        ip = request.META['REMOTE_ADDR']
        print ('request_query:',1,request,2,request.method,3,request.body,4,request.path_info,5,request.is_ajax(),6,ip)
        if request.method != 'POST':
            return HttpResponse(json.dumps({'status':100, 'msg': '请求方式错误'}))
        username = request.POST.get('userName', None)
        password = request.POST.get('password', None)
        print ('search_query:',username,password,type(username),type(password))
        query = models.UserInfo.objects.filter(username=username,status=1,useing=1).values()
        try:
            if query.__len__() > 0:
                if query[0]['password'] == password:
                    userid = query[0]['id']
                    request.session['username'] = username
                    request.session['user_id'] = userid
                    request.session['is_login'] = True
                    request.session.set_expiry(30 * 60)
                    models.UserInfo.objects.filter(username=username).update(old_login_time=datetime.datetime.today())
                    response = json.dumps({'status':1,'msg':'登录成功','data':username})
                    return HttpResponse(response)
                elif query[0]['password'] != password:
                    return HttpResponse(json.dumps({'status':2, 'msg': '密码错误'}))
            elif query.__len__() == 0:
                return HttpResponse(json.dumps({'status':3, 'msg': '用户未注册'}))
            else:
                return HttpResponse(json.dumps({'status':500, 'msg':'error'}))
        except BaseException as e:
            e = str(e)
            return HttpResponse(json.dumps({'status':500, 'msg': e}))