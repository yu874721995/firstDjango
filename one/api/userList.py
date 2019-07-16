#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/7/10 20:47
@Author  : Careslten
@Site    : 
@File    : userList.py
@Software: PyCharm
'''


from django.http import HttpResponse
from one import models
import json,time
from Public.JsonData import DateEncoder

class user_list():

    def userList(self,request):
        query = []
        query_list = models.UserInfo.objects.filter(useing=1).values()
        print('aaaaaaaaaa',query_list)
        for i in query_list:
            a = {}
            a['id'] = i['id']
            a['status'] = i['status']
            a['username'] = i['username']
            a['sex'] = i['sex']
            a['old_login_time'] = i['old_login_time'].strftime('%Y-%m-%d %H:%M:%S')
            query.append(a)
        print('查询出的所有用户:', query)
        return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data': query}))

    def session_test(self,request):
        username = request.session.get('username', None)  # 取这个key的值，如果不存在就为None
        userid = request.session.get('user_id', None)
        times = time.strftime('%y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        return HttpResponse(
            json.dumps({'status': 1, 'msg': '操作成功', 'data': {'username': username, 'userid': userid, 'time': times}}))

    def getuser(self,request):
        username = request.session.get('username', None)
        return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data': {'username': username}}))

    def userHistory(self,request):
        username = request.session.get('username', 1)
        search = request.POST.get('search',None)
        user_host_history = ''
        if username == 1:
            return HttpResponse(json.dumps({'status': 1, 'msg': '登录过期'}))
        user_id = models.UserInfo.objects.get(username=username).id
        print(search=='')
        print(search)
        if search == '' or search == None:
            user_host_history = models.user_host.objects.filter(userid=user_id, status=1).values()

        else:
            user_host_history = models.user_host.objects.filter(userid=user_id, status=1,
                                                                casename__icontains=search).values()
        user_history = []
        for i in user_host_history:
            everyhost = {}
            body = {}
            header = {}
            host_id = i['id']
            body_init = models.user_body.objects.filter(host_id_id=host_id, type=1, status=1).values()
            header_init = models.user_body.objects.filter(host_id_id=host_id, type=2, status=1).values()
            for everybody in body_init:
                body[everybody['key']] = everybody['value']
            for everheader in header_init:
                header[everheader['key']] = everheader['value']
            everyhost['id'] = i['id']
            everyhost['host'] = i['host']
            everyhost['body'] = body
            everyhost['header'] = header
            everyhost['create_date'] = i['create_date']
            everyhost['response_body'] = i['response_body']
            everyhost['type'] = i['method']
            everyhost['CaseName'] = i['casename']
            user_history.append(everyhost)
        return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data': user_history}, cls=DateEncoder))

    def add_User(self,request):
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username  == None or password == None:
            return HttpResponse(json.dumps({'status': 500, 'msg': '参数错误'}))
        query = models.UserInfo.objects.filter(username=str(username))
        if query.__len__() >= 1:
            return HttpResponse(json.dumps({'status': 500,'msg': '用户已存在'}))
        try:
            dic = {'username':username, 'password':password}
            models.UserInfo.objects.create(**dic)
            return HttpResponse(json.dumps({'status': 1, 'msg':'操作成功'}))
        except Exception as e:
            return HttpResponse(json.dumps({'status': 500, 'msg':e}))

    def userDelList(self, request):
        query = []
        try:
            query_list = models.UserInfo.objects.filter(useing=0).values()
            print('ddddddddd', query_list)
            for i in query_list:
                a = {}
                a['id'] = i['id']
                a['status'] = i['status']
                a['username'] = i['username']
                a['sex'] = i['sex']
                a['create_time'] = i['create_time'].strftime('%Y-%m-%d %H:%M:%S')
                query.append(a)
            print('查询出的所有已删除用户:', query)
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'status': 1, 'msg':e}))
        return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data': query}))

    def recoverCustomer(self,request):
        user_id = request.POST.get('user_id',None)
        if user_id == None:
            return HttpResponse(json.dumps({'status': 500, 'msg': '参数错误'}))
        try:
            models.UserInfo.objects.filter(id=user_id).update(useing=1)
        except Exception as e:
            return HttpResponse(json.dumps({'status': 500, 'msg': e}))
        return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功'}))