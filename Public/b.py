#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/8/8 10:37
@Author  : Careslten
@Site    : 
@File    : b.py
@Software: PyCharm
'''
from Public.a import *
import multiprocessing,ddt,os,unittest,requests


data = {
    'token':'noget',
    'timestamp':1566556563133,
    'telephone':'15989510965',
    'code':8532,
    'appKey':'FFFF0N0000000000829A',
    'sessionId':'01c67T1BCn-c9mKDdKrkhhVM1gDxJncQYuDkBhpFYjW27sqF2zsXLhZ2kRs-Y7bBLwU70MljKKd8Mz86Z3GzVPV4FKIHMRl2s36_NFYZovyrcYnk3qKCBtQisNJpQ8M66He-b0cRzOcuGHm3U2fzMq2z7Q1KSsr2zo_Uw_3zbDy4eLTuh8Odnajr6mPZFTM_jg',
    'sigToken':'1566556547344:0.023529607523515628',
    'sig':'05XqrtZ0EaFgmmqIQes-s-CJXwNEdiT3l4T1BnGWs-OFR0zGcDjvyJWSmVJE2Ry-QqrfeKflbbPL2KPdV1IyhghTIGCwCjH32UT3_TCFrWdtoPmeEq0r1kSo3gwyX1KM2XVxpTlyI4uVcGvhMw3eV2xVT1kLBE0I1FDf55EUSpe1QYcMU2uq9DWmtcS8eQu44G8MVGGV8FtWa3tzyS3AQZ_20DF2aKPHUOS6qcq1dKreCPTIbEIsfU9MTx6Fa3_1W1rCs7_xyLKM70g4YJWjY6Rn6lHRiaBihVn7GRRP2A5mB9e_7YfbOph4zFYYnccV5zUlsGWrTOJhnM97adElsO3uQNBaSrJ8IPsm5krgosK84Vx_2CP6ezboh0b4rfNaUjJAya_-aILE1QkvnQkc2RmTwtx_mThOqOO4tEOYMnotM',
    'scene':'ic_message',
    'sign':'5C1374DB197005A121186DEBA9CA5AE5'
}

r= requests.post('https://test.cpyzj.com/req/cpyzj/user/getPCSmsForRegist',data)
print(r.json())