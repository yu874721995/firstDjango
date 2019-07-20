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

    #添加产品或添加模块
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
            subjection = request.POST.get('subjection',None)
            if subjection == '' or subjection == None:
                return HttpResponse(json.dumps({'status': 200, 'msg': '必须选择上级产品'}))
            try:
                dic = {'type':'2', 'name': cpname,'subjection':subjection }
                models.casecp_mk.objects.create(**dic)
                return HttpResponse(json.dumps({'status':1, 'msg': '操作成功'}))
            except Exception as e:
                print('error----------------1',e)
                return HttpResponse(json.dumps({'status':1, 'msg': '数据库错误'}))

    #查询产品及模块列表
    def queryForProduct(self,request):
        #仅查询产品列表
        query = models.casecp_mk.objects.filter(status=1,type=1).values()
        data = []
        for item in query:
            mores = {}
            mores['id'] = item['id']
            mores['type'] = item['type']
            mores['name'] = item['name']
            mores['create_date'] = item['create_date']
            data.append(mores)
        print('response==================',data)
        return HttpResponse(json.dumps({'status':1, 'msg': '操作成功','data':data},cls=DateEncoder))

    def queryForOur(self,request):
        querys = models.casecp_mk.objects.filter(status=1, type=1).values()
        data = []
        for items in querys:
            mores = {}
            mores['name'] = items['name']
            mores['value'] = items['id']
            query = models.casecp_mk.objects.filter(status=1, type=2,subjection=items['id']).values()
            datas = []
            for item in query:
                more = {}
                more['value'] = item['id']
                more['name'] = item['name']
                datas.append(more)
            mores['children'] = datas
            data.append(mores)
        return HttpResponse(json.dumps({'code': 0, 'data': data,'msg': 'success'}))












