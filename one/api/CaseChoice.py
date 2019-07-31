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
        query_cp = models.casecp_mk.objects.filter(name=cpname,status=1,type=1).values()
        #如果已存在则无法添加
        if len(query_cp) != 0:
            return HttpResponse(json.dumps({'status':200, 'msg': '该产品已存在'}))
        if types == 1 or types == '1':
            try:
                dic = {'type':'1', 'name': cpname, }
                models.casecp_mk.objects.create(**dic)
                return HttpResponse(json.dumps({'status':1, 'msg': '操作成功'}))
            except Exception as e:
                print('error----------------1',e)
                return HttpResponse(json.dumps({'status':1, 'msg': '数据库错误'}))

            #添加模块
        else:
            subjection = request.POST.get('subjection',None)
            query_mk = models.casecp_mk.objects.filter(name=cpname, status=1, type=2, subjection=subjection).values()
            if len(query_mk) != 0:
                return HttpResponse(json.dumps({'status':200, 'msg': '该模块已存在'}))
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


    def caseList(self,request):
        user_id = request.session.get('user_id',None)
        if user_id == None:
            return HttpResponse(json.dumps({'status':100,'msg': '登录过期'}))
        caseHost = models.user_TestCase_host.objects.all().values()
        data = []
        for i in caseHost:
            case_data = {}
            case_data['case_id'] = i['id']
            case_data['status'] = i['status']
            case_data['caseName'] = i['caseName']
            case_data['host'] = i['host']
            case_data['create_date'] = i['create_date']
            username = models.UserInfo.objects.filter(id=user_id).values()[0]['username']
            case_data['username'] = username
            case_data['method'] = i['method']
            mk = models.casecp_mk.objects.filter(id=i['subjectionId']).values()[0]
            cp = models.casecp_mk.objects.filter(id=mk['subjection']).values()[0]['name']
            case_data['subjection_cp'] = cp
            case_data['subjection_mk'] = mk
            case_data['create_date'] = i['create_date']
            #在这里添加assert和body、header的内容
            ###
            data.append(case_data)
        print(data)

        return HttpResponse(json.dumps({'status':1,'msg': '操作成功','data':{'h':1}}))











