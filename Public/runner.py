#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11:45
# @Author  : Carewn
# @Software: PyCharm

from Public import HTMLTestRunner_Rewrite
import unittest
import time,os
import sys
print (sys.argv[0])

report_path = os.path.dirname(os.path.abspath('.'))+'/interFace/Test_report/'
report_time = time.strftime('%y-%m-%d-%H-%M-%S',time.localtime(time.time()))
report_name = 'D:\pyfold\interFace\Test_report\\'+str(report_time)+"-Test_report.html"
fp = open(report_name,'wb')


testsuite = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover('C_TestCase',pattern='test_*.py',top_level_dir=None)
for testsuites in discover:
    for i in testsuites:
        testsuite.addTest(i)

runner = HTMLTestRunner_Rewrite.HTMLTestRunner(['sdasdsad','asdsadsadsadsadasd'],stream=fp,title='自动化测试报告',description='用例执行情况')
print(testsuite)
runner.run(testsuite)




