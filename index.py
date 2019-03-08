# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File    : index.py
# @Author  : WSQ
# @Time    : 2019/3/2 12:07

import json

json = '''
{
    'name': 'WSQ',
    'age': '18'
}
'''
jsonText = json.loads(json)
print(jsonText.get('name'))
