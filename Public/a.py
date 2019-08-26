#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/8/8 10:36
@Author  : Careslten
@Site    : 
@File    : a.py
@Software: PyCharm
'''

from ruamel import yaml
import os,json

class read_yaml():

    def read(self):
        # file = open(os.path.dirname(os.path.abspath('.')) + '/Public/case_date.yaml')
        # file = open(os.path.abspath('.')+'/Public/case_date.yaml','rb')
        # cont = file.read()
        # text = yaml.load(cont)
        # item = []
        # for i in list(text):
        #     item.append(text[i])
        item = []
        with open(os.path.abspath('.') + '/Public/case_date.json', 'r') as f:
            load_dict = json.load(f)
            f.close()
        self.load_dict = load_dict
        print(self.load_dict)
        for i in list(self.load_dict):
            item.append(self.load_dict[i])
        return item



