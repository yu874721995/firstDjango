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
import json,os,time
from Public.JsonData import DateEncoder
from django.forms.models import model_to_dict
from ruamel import yaml
from Public.runner import runner_case

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


    #用例列表
    def caseList(self,request):
        user_id = request.session.get('user_id',None)
        page = request.POST.get('page',None)
        limit = request.POST.get('limit',None)
        fy = self.pages(page,limit)
        if user_id == None:
            return HttpResponse(json.dumps({'status':100,'msg': '登录过期'}))
        caseHost = models.user_TestCase_host.objects.all().values().order_by('status','-create_date')
        count = models.user_TestCase_host.objects.all().count()
        data = []
        #处理用例数据
        num = 0
        for i in caseHost:
            num += 1
            if num < fy[0]:
                continue
            if num > fy[1]:
                break
            case_body = {}
            case_header = {}
            case_asserts = {}
            case_data = {}
            case_data['case_id'] = i['id']
            case_data['status'] = i['status']
            case_data['caseName'] = i['caseName']
            case_data['host'] = i['host']
            case_data['create_date'] = i['create_date']
            username = models.UserInfo.objects.filter(id=i['userid']).values()[0]['username']
            case_data['username'] = username
            case_data['method'] = i['method']
            mk = models.casecp_mk.objects.filter(id=i['subjectionId']).values()[0]
            mk_name = mk['name']
            cp = models.casecp_mk.objects.filter(id=mk['subjection']).values()[0]['name']
            case_data['subjection_cp'] = cp
            case_data['subjection_mk'] = mk_name
            case_data['create_date'] = i['create_date']

            #在这里添加assert和body、header的内容
            body = models.user_TestCase_body.objects.filter(host_id=i['id'],type=1).values()
            for a in body:
                case_body[a['key']] = a['value']
            case_data['case_body'] = case_body

            header = models.user_TestCase_body.objects.filter(host_id=i['id'],type=2).values()
            for b in header:
                case_header[b['key']] = b['value']
            case_data['case_header'] = case_header

            asserts = models.user_Case_Assert.objects.filter(host_id=i['id']).values()
            asserts_count = models.user_Case_Assert.objects.filter(host_id=i['id']).count()
            for c in asserts:
                case_asserts[c['Assert_name']] = c['Assert_text']
            case_asserts['count'] = asserts_count
            case_data['case_assert'] = case_asserts


            data.append(case_data)

        return HttpResponse(json.dumps({'code':0,'count':count,'data':data,'msg':'操作成功','status':1},cls=DateEncoder))

    #分页
    def pages(self,page,limit):
        page = int(page)
        limit = int(limit)
        if page == 1:
            return (1,limit)
        begin = (page - 1) * limit + 1
        end = page * limit
        return (begin,end)

    #执行用例
    def batchExecution(self,request):
        user_id = request.session.get('user_id',None)
        if user_id == None:
            return  HttpResponse(json.dumps({'status':100,'msg': '登录过期'}))
        caseId = request.POST.get('caseId',None).lstrip('[').rstrip(']').split(',')
        date = self.query_case(caseId)
        # path = os.path.dirname(os.path.abspath('.')) + '/Public/case_date.yaml'

        # path = os.path.abspath('.') + '/Public/case_date.yaml'
        path = os.path.abspath('.') + '/Public/case_date.json'
        datas = {}
        case_name = []
        num = 0
        isOk = False
        for i in date:
            i = eval(repr(i).replace('\\',''))
            datas[num] = i
            case_name.append(i['caseName'])
            num += 1
        try:
            # with open(path,'w',encoding='utf-8') as f:
            #     yaml.dump(datas,f,Dumper=yaml.RoundTripDumper)
            #     isOk = True
            #     print('asdsadsadasdada')

            # result = yaml.safe_dump(datas, encoding='utf-8', allow_unicode=True, default_flow_style=False)
            # open(path,'wb').write(result)

            with open(path,'w') as f:
                json.dump(datas,f)
                f.close()
            isOk = True
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'status':500,'msg': '~出错了，请重试'}))
        # self.query_case(caseId)
        # 执行测试
        report_name = ''
        if isOk == True:
            report_name = runner_case().run(case_name=case_name)
        dic = {
            'report_name':report_name,'becuxe_id':str(caseId),'type':1
        }
        try:
            models.Case_report.objects.create(**dic)
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'status':500,'msg': '出错了，请重试'}))
        return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功'}))


    #获取需要执行的用例数据
    def query_case(self,caseId):
        case_data = models.user_TestCase_host.objects.filter(id__in=caseId,status=1)
        data = []
        for i in case_data:
            i = model_to_dict(i)
            case_body = {}
            case_header = {}
            case_asserts = {}
            case_data = {}
            case_data['case_id'] = i['id']
            case_data['status'] = i['status']
            case_data['caseName'] = i['caseName']
            case_data['host'] = i['host']
            username = models.UserInfo.objects.filter(id=i['userid']).values()[0]['username']
            case_data['method'] = i['method']

            # 在这里添加assert和body、header的内容
            body = models.user_TestCase_body.objects.filter(host_id=i['id'], type=1).values()
            for a in body:
                case_body[a['key']] = a['value']
            case_data['case_body'] = case_body
            header = models.user_TestCase_body.objects.filter(host_id=i['id'], type=2).values()
            for b in header:
                case_header[b['key']] = b['value']
            case_data['case_header'] = case_header
            asserts = models.user_Case_Assert.objects.filter(host_id=i['id']).values()
            asserts_count = models.user_Case_Assert.objects.filter(host_id=i['id']).count()
            for c in asserts:
                case_asserts[c['Assert_name']] = c['Assert_text']
            case_data['case_assert'] = case_asserts
            data.append(case_data)
        return data






