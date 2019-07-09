"""twostr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import re_path
from django.urls import path
from one import views as indexviews
from one.user_CreateTestCase import user_testCase as SaveCase


urlpatterns = [
    #re_path('',oneviews.login),
    re_path(r'^$',indexviews.login),
    re_path('session_test',indexviews.session_test),
    re_path('index',indexviews.index),
    re_path('login',indexviews.login),
    re_path('Loginup',indexviews.Loginup),
    re_path('goRegister',indexviews.goRegister),
    re_path('register',indexviews.register),
    re_path('reqJson',indexviews.reqJson),
    re_path('username',indexviews.getuser),
    re_path('UserHistory', indexviews.userHistory),
    re_path(r'^accounts/login/$',indexviews.login),
    re_path('SaveTestCase',SaveCase().saveTestCase),
    re_path('deletecase',indexviews.deletecase),
    re_path('userList',indexviews.userList),
]







from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from one.siteathome import task

sched = BackgroundScheduler()
sched.add_jobstore(DjangoJobStore(),'default')

@register_job(sched,'cron',second='10')
def my_task():
    task.deletesession()
try:
    register_events(sched)
    sched.start()
except Exception as e:
    sched.shutdown()
