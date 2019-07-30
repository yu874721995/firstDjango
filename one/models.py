from django.db import models
from datetime import datetime
import django.utils.timezone as timezone

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    status = models.CharField(max_length=20, default=1)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, default=1)
    create_time = models.DateTimeField(default=timezone.now)
    old_login_time = models.DateTimeField(default=timezone.now)
    useing = models.CharField(max_length=20, default=1)
# Create your models here.
class user_host(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    status = models.CharField(max_length=20,default=1)
    host = models.CharField(max_length=200,blank=False)
    create_date = models.DateTimeField(default=timezone.now)
    response_body = models.TextField(max_length=200,default='ZZZ')
    userid = models.IntegerField()
    method = models.CharField(max_length=20,default='post')
    json_body = models.CharField(max_length=200, blank=False, default='')
    json_header = models.CharField(max_length=200, blank=False, default='')
    casename = models.CharField(max_length=100,default='暂无名称')

class user_body(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    status = models.CharField(max_length=20, default=1)
    key = models.CharField(max_length=200,blank=False)
    value = models.CharField(max_length=200,blank=False)
    host_id = models.ForeignKey('user_host',on_delete=models.CASCADE)
    type = models.CharField(max_length=10,default=1)

class user_TestCase_host(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    status = models.CharField(max_length=20, default=1)
    caseName = models.CharField(max_length=200, blank=False)
    host = models.CharField(max_length=200, blank=False)
    create_date = models.DateTimeField(default=timezone.now)
    userid = models.IntegerField()
    method = models.CharField(max_length=20, default='post')
    subjectionId = models.CharField(max_length=200, blank=False,default='')

class casecp_mk(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    status = models.CharField(max_length=20, default=1)
    type = models.CharField(max_length=20, default=1)
    name = models.CharField(max_length=200, blank=False)
    subjection = models.CharField(max_length=20, default='')
    create_date = models.DateTimeField(default=timezone.now)

class user_TestCase_body(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    status = models.CharField(max_length=20, default=1)
    key = models.CharField(max_length=200, blank=False)
    value = models.CharField(max_length=200, blank=False)
    host_id = models.ForeignKey('user_TestCase_host', on_delete=models.CASCADE)

class user_Case_Assert(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    status = models.CharField(max_length=20, default=1)
    Assert_name = models.CharField(max_length=200, blank=False,default='')
    Assert_text = models.CharField(max_length=200, blank=False,default='')
    host_id = models.ForeignKey('user_TestCase_host', on_delete=models.CASCADE)

