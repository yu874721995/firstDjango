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
import requests
from ddt import ddt,file_data


@ddt
class Test_clubList(unittest.TestCase):
    def case_id(self,date):

        return date

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @file_data('case_date.yaml')
    def test_case(cls,**value):
        url = value['host']

        r =requests.post()



if __name__ == '__main__':
    unittest.main()