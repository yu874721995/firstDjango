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

    def saveTestCase(self,request):
        print('-------------request_body:',request.POST)
        url = request.POST.get('url',None)
        data = request.POST.get('data[]',None)
        type = request.POST.get('type',None)
        if url == None or url is False or url == '' or data == None or data is False or data == '' or type == None or type is False or type == '':
            return HttpResponse(json.dumps({'status':5,'msg':'参数错误'}))

        return HttpResponse(json.dumps({'status':1,'msg':'ok'}))

