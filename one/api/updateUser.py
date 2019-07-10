#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/7/10 20:42
@Author  : Careslten
@Site    : 
@File    : updateUser.py
@Software: PyCharm
'''
from django.http import HttpResponse
from one import models
import json


class update_Users():

    def updateUserStatus(self,request):
        types = request.POST.get('type', None)
        user_id = request.POST.get('user_id', None)
        print('dddddddddeeeeeeebbbbbbuuuuuggggg', types, user_id)
        if types == None or user_id == None:
            print(1111111)
            return HttpResponse(json.dumps({'status': 500, 'msg': '参数错误'}))
        if types == 1 or types == '1':
            models.UserInfo.objects.filter(id=user_id).update(status=1)
        elif types == 0 or types == '0':
            models.UserInfo.objects.filter(id=user_id).update(status=0)
        else:
            print(2222222)
            return HttpResponse(json.dumps({'status': 500, 'msg': '参数错误'}))
        return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功'}))