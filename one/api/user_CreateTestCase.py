#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/5/28 11:47
@Author  : Careslten
@Site    : 
@File    : user_CreateTestCase.py
@Software: PyCharm
'''

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import pymysql as mysql
import json,time
from one import models
import requests
from Public.JsonData import DateEncoder
from django.contrib.auth.decorators import login_required

class user_testCase():

    def checkquery(self,*args):
        for i in args:
            if i == None or i is False or i == '':
                return True

    def saveTestCase(self,request):
        print('-------------request_body:',request.POST)
        caseName = request.POST.get('caseName',None) #用例名称
        cpChoice = request.POST.get('cpChoice',None)
        caseUrl = request.POST.get('caseUrl',None)#用例host
        method = request.POST.get('method',None)#用例method 1为get 2为post
        body = request.POST.get('body', None)
        header = request.POST.get('header', None)
        assertName = request.POST.getlist('assertName', None)
        assertText = request.POST.getlist('assertText', None)
        user_id = request.session.get('user_id', None)
        print('caseName:',caseName,'cpChoice:',cpChoice,'caseUrl:',caseUrl,'method:',method,'body:',body,'header:',header,'assertName:',assertName,'assertText:',assertText)
        #参数校验
        if self.checkquery([caseName,cpChoice,caseUrl,assertName,assertText,method]):
            return HttpResponse(json.dumps({'status':5,'msg':'参数错误'}))
        if user_id == None:
            return HttpResponse(json.dumps({'status': 100, 'msg': '登录过期'}))

        cpChoice_mk = cpChoice.split('/')[1] #隶属模块

        #处理传入的body
        data = {}#data
        print((':' in body or ":" in body) and '["' not in body)
        if body == '' or body == None:#body为空时直接跳过
            pass
        else:
            if (':' in body or ":" in body) and '["' not in body:
                try:
                    data = eval(body)
                except Exception as e:
                    return HttpResponse(json.dumps({'status': 500, 'msg': '传入参数有误'}))
            else:
                for item in body.split('","'):
                    item = item.lstrip('["').rstrip('"]')
                    data[item.split('--')[0]] = item.split('--')[1]

        #处理header
        headers = {}#header
        if header == None or header == '': #header为空时直接跳过
            pass
        else:
            if (':' in header or ":" in header) and '["' not in header:
                try:
                    headers = eval(header)
                except Exception as e:
                    return HttpResponse(json.dumps({'status': 500, 'msg': '传入参数有误'}))
            else:
                for item in header.split('","'):
                    item = item.lstrip('["').rstrip('"]')
                    headers[item.split('--')[0]] = item.split('--')[1]

        CaseAssert = {} #断言dict
        assertName = assertName[0].lstrip('["').rstrip('"]').split(',')
        assertText = assertText[0].lstrip('["').rstrip('"]').split(',')
        if len(assertText) == 0:
            pass
        else:
            for x,y in zip(assertName,assertText):
                #需要处理掉前端传入的"
                x = x.replace('"','')
                y = y.replace('"','')
                CaseAssert[x] = y

        dic = {
            'caseName':caseName,'host':caseUrl,'userid':user_id,'method':method,'subjectionId':cpChoice_mk
        }
        models.user_TestCase_host.objects.create(**dic)
        host = models.user_TestCase_host.objects.filter(host=caseUrl).order_by('-create_date')
        host_id = host.values()[0]['id']

        try:
            for item in data.keys():
                dic_body = {
                        'key':item,'value':data[item],'host_id_id':host_id,'type':1
                }
                models.user_TestCase_body.objects.create(**dic_body)
        except Exception as e:
            print(e)
            print('data:-----------',data)
            return HttpResponse(json.dumps({'status': 500, 'msg': '存入data数据库错误'}))
        try:
            for item in headers.keys():
                dic_header = {
                    'key': item, 'value': headers[item], 'host_id_id': host_id, 'type': 2
                }
                models.user_TestCase_body.objects.create(**dic_header)
        except Exception as e:
            return HttpResponse(json.dumps({'status': 500, 'msg': '存入header数据库错误'}))
        try:
            for item in CaseAssert.keys():
                dic_assert = {
                    'Assert_name': item, 'Assert_text': CaseAssert[item], 'host_id_id': host_id
                }
                models.user_Case_Assert.objects.create(**dic_assert)
        except Exception as e:
            print('error------------',e)
            return HttpResponse(json.dumps({'status': 500, 'msg': '存入assert数据库错误'}))
        return HttpResponse(json.dumps({'status':1,'msg':'操作成功'}))




