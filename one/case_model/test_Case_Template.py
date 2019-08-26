#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/8/6 16:06
@Author  : Careslten
@Site    : 
@File    : test_Case_Template.py
@Software: PyCharm
'''
import unittest
import requests,os
from ddt import ddt,data,unpack
from Public.logger import Logger
from Public.a import read_yaml

mylog = Logger('mylog').getlog()
item = read_yaml()
@ddt
class Test_clubList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*item.read())
    @unpack
    # @file_data(os.path.abspath('.') + '/Public/case_date.yaml')
    def test_case(cls,case_id,status,caseName,host,method,case_body,case_header,case_assert):
        pass



if __name__ == '__main__':
    unittest.main()