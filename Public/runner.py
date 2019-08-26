#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11:45
# @Author  : Carewn
# @Software: PyCharm

from Public import HTMLTestRunner_Rewrite
import unittest
import time,os
import sys

class runner_case():

    def run(self,case_name):
        # report_path = os.path.abspath('.')+'/one/Test_report/'
        # report_path = os.path.dirname(os.path.abspath('.')) + '/one/Test_report/'
        report_path = os.path.abspath('.') + '/one/Test_report/'
        report_time = time.strftime('%y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        report_name = report_path+str(report_time)+"-Test_report.html"
        fp = open(report_name,'wb')
        testsuite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover('case_model',pattern='test_*.py',top_level_dir='one')
        for testsuites in discover:
            for i in testsuites:
                print('套件里面加1')
                testsuite.addTest(i)
        # path = os.path.dirname(os.path.abspath('.')) + 'twostr/one/case_model'
        # path = 'E:\\twostr/one/case_model'
        # discover = unittest.defaultTestLoader.discover(path,pattern='test*.py')
        runner = HTMLTestRunner_Rewrite.HTMLTestRunner(case_name,stream=fp,title='自动化测试报告',description='用例执行情况')
        runner.run(testsuite)
        # runner.run(discover)
        return report_name




