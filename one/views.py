from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import pymysql as mysql
import json,time
from one import models
import requests

from django.contrib.auth.decorators import login_required
import datetime

user_list = []

def login(request):
    return render(request,'login.html')

def index(request):
    session_user = request.session.get('username',None)
    if session_user is None:
        return render(request, 'login.html')
    return render(request,'index.html')


def goRegister(request):
    return render(request,'register.html')




def register(request):
    username = request.POST.get('userName',None)
    password = request.POST.get('password',None)
    query = models.UserInfo.objects.filter(user=str(username))
    if query.__len__() >= 1:
        return HttpResponse(json.dumps({'status':2,
                                        'msg':'用户已注册'}))
    elif query.__len__() == 0:
        try:
            models.UserInfo.objects.create(user=username, password=password)
            session_username = models.UserInfo.objects.filter(user=username).values()
            request.session['user_id'] = session_username[0]['id']
            request.session['username'] = session_username[0]['user']
            request.session['is_login'] = True
            request.session.set_expiry(30 * 60)
            return HttpResponse(json.dumps({'status': 1,
                                            'msg': '注册成功','data':username}))
        except Exception as e:
            return HttpResponse(json.dumps({'status': 3,
                                            'msg': '注册失败'}))

def deleteHistory(request):
    user_id = request.session.get('user_id', None)
    if user_id is None or user_id == '1':
        return HttpResponse(json.dumps({'status': 200, 'msg': '登录超时'}))
    case_id = request.POST.get('caseId',None)
    models.user_body.objects.filter(host_id_id=case_id).update(status=0)
    models.user_host.objects.filter(id=case_id).update(status=0)
    return HttpResponse(json.dumps({'status':1,'msg':'操作成功'}))



def x():
    #查询
    a = models.UserInfo.objects.all()#查询所有数据
    print (a)
    b = models.UserInfo.objects.all().values('user')#查询user列所有数据
    c = models.UserInfo.objects.all().values_list('id','user') #取出id和user列，并生成一个列表
    d = models.UserInfo.objects.get(id=1)#查询单条？？
    d = models.UserInfo.objects.get(user='yu')
    #增
    e = models.UserInfo.objects.create(user='yu',password='123456')or models.UserInfo(user='yu',password='123456')
    #或者
    dic = {'user':'yu','password':'123456'}
    models.UserInfo.objects.create(**dic)
    #删除
    models.UserInfo.objects.filter(user='yu').delete()
    #改
    models.UserInfo.objects.filter(user='yu').update(password='12345678')
    #或者
    s = models.UserInfo.objects.get(user='yu')
    s.pwd='123456'
    s.save()
#获取个数
    models.UserInfo.objects.filter(name='yu').count()
    models.UserInfo.objects.filter(id__gt=1)#id大于1
    models.UserInfo.objects.filter(id__lt=10)#ID小于10
    models.UserInfo.objects.filter(id__lt=10, id__gt=1)#id小于10且id大于1

    #in
    models.UserInfo.objects.filter(id__in=[11, 22, 33])#  in11,22,33
    models.UserInfo.objects.exclude(id__in=[11, 22, 33])#not in

    #匹配
    models.UserInfo.objects.filter(user__contains='yu')
    models.UserInfo.objects.filter(user__icontains='yu')
    models.UserInfo.objects.exclude(name__icontains="ven")
    #bettwen and
    models.UserInfo.objects.filter(id__range=[1, 2])# 范围bettwen and
    #order by
    models.UserInfo.objects.filter(name='seven').order_by('id')
    models.UserInfo.objects.filter(name='seven').order_by('-id')
    #limit
    q = models.UserInfo.objects.all()[10:20]
    #group by
    from django.db.models import Count,Min,Max,Sum
    models.UserInfo.objects.filter(c1=1).values('id').annotate(c=Count('num'))

    # #时间格式的用法
    # #from django.db import models
    # s = models.DatetimeFeild
    # auto_now = True ：则每次更新都会更新这个时间
    # auto_now_add则只是第一次创建添加，之后的更新不再改变。
    # 例如：
    # class UserInfo(models.Model):
    #     name = models.CharField(max_length=32)
    #     ctime = models.DateTimeField(auto_now=True)
    #     uptime = models.DateTimeField(auto_now_add=True)
    # null = True,允许该列为空
    # blank = True 允许admin后台中为空
    '''新增加表中字段时，设置默认值，不会导致表中数据错乱'''
    # #ip
    # ip = models.GenericIPAddressField(protocol="ipv4", null=True, blank=True)
    # #img图片
    # img = models.ImageField(null=True, blank=True, upload_to="upload")

    #连表
    # 一对多：models.ForeignKey(其他表)
    # 多对多：models.ManyToManyField(其他表)
    # 一对一：models.OneToOneField(其他表)








