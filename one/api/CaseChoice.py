#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/7/18 20:11
@Author  : Careslten
@Site    : 
@File    : CaseChoice.py
@Software: PyCharm
'''
from django.http import HttpResponse
from one import models
import json,time
from Public.JsonData import DateEncoder

class caseChoice():


    def addChoice(self,request):
        cpname = request.POST.get('cpname',None)
        types = request.POST.get('type',None)
        if cpname == '' or cpname == None or types == '' or types == None:
            return HttpResponse(json.dumps({'status':200, 'msg': '名称或类型不能为空'}))
        if types == 1 or types == '1':
            try:
                dic = {'type':'1', 'name': cpname, }
                models.casecp_mk.objects.create(**dic)
                return HttpResponse(json.dumps({'status':1, 'msg': '操作成功'}))
            except Exception as e:
                print('error----------------1',e)
                return HttpResponse(json.dumps({'status':1, 'msg': '数据库错误'}))
        else:
            return HttpResponse(json.dumps({'status':200, 'msg': 'shaodeng'}))


