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
                return False

    def saveTestCase(self,request):
        print('-------------request_body:',request.POST)
        caseName = request.POST.get('caseName',None)
        cpChoice = request.POST.get('cpChoice',None)
        caseUrl = request.POST.get('caseUrl',None)
        method = request.POST.get('method',None)
        body = request.POST.get('body', None)
        header = request.POST.get('header', None)
        assertName = request.POST.get('assertName', None)
        assertText = request.POST.get('assertText', None)

        #参数校验
        if self.checkquery([caseName,cpChoice,caseUrl,assertName,assertText,method]) == False:
            return HttpResponse(json.dumps({'status':5,'msg':'参数错误'}))



