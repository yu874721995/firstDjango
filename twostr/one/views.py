from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import pymysql as mysql
import json,time
from one import models
import requests
from Public.JsonData import DateEncoder
from django.contrib.auth.decorators import login_required

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

def Loginup(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    query = models.UserInfo.objects.filter(user=username).values()
    try:
        if query.__len__() > 0:
            if query[0]['password'] == password:
                userid = query[0]['id']
                request.session['username'] = username
                request.session['user_id'] = userid
                request.session['is_login'] = True
                request.session.set_expiry(0)
                response = json.dumps({'status':1,'msg':'登录成功','data':username})
                return HttpResponse(response)
            elif query[0]['password'] != password:
                return HttpResponse(json.dumps({'status':2, 'msg': '密码错误'}))
        elif query.__len__() == 0:
            return HttpResponse(json.dumps({'status':3, 'msg': '用户未注册'}))
        else:
            return render(request,'login.html')
    except BaseException as e:
        return render(request,'login.html', {})


def register(request):
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)
    query = models.UserInfo.objects.filter(user=username)
    print ('-------------------------已存在{}个用户'.format(list(query).__len__()))
    if query.__len__() >= 1:
        return HttpResponse(json.dumps({'status':2,
                                        'msg':'用户已注册'}))
    elif query.__len__() == 0:
        try:
            models.UserInfo.objects.create(user=username, password=password)
            session_username = models.UserInfo.objects.filter(user=username)
            request.session['user_id'] = session_username[0][0]
            request.session['username'] = session_username[0][1]
            request.session['is_login'] = True
            request.session.set_expiry(1000)
            return HttpResponse(json.dumps({'status': 1,
                                            'msg': '注册成功','data':username}))
        except Exception as e:
            return HttpResponse(json.dumps({'status': 3,
                                            'msg': '注册失败'}))


def session_test(request):
    username = request.session.get('username',None)#取这个key的值，如果不存在就为None
    userid = request.session.get('userid',None)
    #s = request.session.session_key
    #request.session.clear_expired()
    return HttpResponse(json.dumps({'status':1,'msg':'操作成功','data':{'username':username,'userid':userid}}))

def getuser(request):
    username = request.session.get('username',None)
    return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data':{'username':username}}))


def userHistory(request):
    username = request.session.get('username',1)
    if username == 1:
        return HttpResponse(json.dumps({'status': 1, 'msg': '登录过期'}))
    user_id = models.UserInfo.objects.get(user=username).id
    user_host_history = models.user_host.objects.filter(userid=user_id).values()
    user_history = []
    for i in user_host_history:
        everyhost = {}
        body = {}
        host_id = i['id']
        body_init = models.user_body.objects.filter(host_id_id=host_id).values()
        for everybody in body_init:
            body[everybody['key']] = everybody['value']
        everyhost['id'] = i['id']
        everyhost['host'] = i['host']
        everyhost['body'] = body
        everyhost['create_date'] = i['create_date']
        everyhost['response_body'] = i['response_body']
        everyhost['type'] = i['type']
        user_history.append(everyhost)
    print (user_history)
    return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data':user_history},cls=DateEncoder))

#处理请求
@login_required
def reqJson(request):
    posturl = request.POST.get('url',None)
    geturl = posturl + '?'
    body = request.POST.getlist('data[]',None)
    user_id = request.session.get('user_id', '1')
    type = request.POST.get('type',None)
    print ('request_body:','url:',posturl,'body:',body,'user_id:',user_id,'type:',type)
    if user_id == '1':
        return HttpResponse(json.dumps({'status': 1, 'msg': '登录超时'}))
    data = {}
    for i in body:
        data[i.split(':')[0]] = i.split(':')[1]
        geturl += i.split(':')[0] + '=' + i.split(':')[1]
    resopnse_body = ''
    #存入历史
    try:
        dic = {'host': posturl, 'userid': user_id, 'response_body': resopnse_body,'type':type}
        print ('------------------------------------',resopnse_body)
        models.user_host.objects.create(**dic)
        #存入body
        host = models.user_host.objects.filter(host=posturl).order_by('-create_date')
        host_id = host.values()[0]['id']
        for i in body:
            dic = {'key':i.split(':')[0],'value':i.split(':')[1],'host_id_id':host_id}
            models.user_body.objects.create(**dic)
    except Exception as e:
        return HttpResponse(json.dumps({'status': 1, 'msg':e,}))
    # 发送请求
    if type == 'post':
        try:
            r = requests.post(posturl, data=data)
            resopnse_body = r.json()
        except Exception as e:
            return HttpResponse(json.dumps({'status': 2, 'msg': '请求错误'}))
    elif type == 'get':
        try:
            r = requests.get(geturl)
            resopnse_body = r.json()
        except Exception as e:
            return HttpResponse(json.dumps({'status': 2, 'msg': '请求错误'}))
    print (resopnse_body)
    return HttpResponse(json.dumps({'status': 1, 'msg': '操作成功', 'data': resopnse_body}))


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








