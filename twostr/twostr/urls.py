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
from one import views as oneviews


urlpatterns = [
    #re_path('',oneviews.login),
    re_path(r'^$',oneviews.login),
    re_path('session_test',oneviews.session_test),
    re_path('index',oneviews.index),
    re_path('login',oneviews.login),
    re_path('Loginup',oneviews.Loginup),
    re_path('goRegister',oneviews.goRegister),
    re_path('register',oneviews.register),
    re_path('reqJson',oneviews.reqJson),
    re_path('user',oneviews.getuser),
    re_path('UserHistory', oneviews.userHistory),
    re_path(r'^accounts/login/$',oneviews.login),
]
