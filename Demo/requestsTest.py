# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File    : requestsTest.py
# @Author  : WSQ
# @Time    : 2019/3/2 23:22

import requests
from requests import Request, Session
import re

# 3.2.1 基本用法
# get请求
'''
r1 = requests.get('https://www.baidu.com')
print(type(r1))
print(r1.status_code)
print(type(r1.text))
print(r1.text)
print(r1.cookies)

data2 = {
    'name': 'WSQ',
    'age': 28
}
r2 = requests.get('http://httpbin.org/get', params=data2)
# 拼接为 http://httpbin.org/get?age=28&name=WSQ
print(r2.text)
print(r2.json())


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r3 = requests.get('https://www.zhihu.com/explore', headers=headers)
print(r3.text)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r3.text)
print(titles)

r4 = requests.get('https://github.com/favicon.ico')
print(r4.text)
print(r4.content)
with open('favicon.ico', 'wb') as f:
    f.write(r4.content)
'''

# post 请求
'''
data = {
    'name': 'WSQ',
    'age': '28'
}
r1 = requests.post('http://httpbin.org/post', data=data)
print(r1.text)

r = requests.get('http://www.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
'''

# 3.2.2 高级用法
# 文件上传
'''
files = {
    'file': open('favicon.ico', 'rb')
}
r1 = requests.post('http://httpbin.org/post', files=files)
print(r1.text)
'''
# cookies
'''
r2 = requests.get('https://www.baidu.com')
print(r2.cookies)
for key, value in r2.cookies.items():
    print(key + '=' + value)

headers = {
    'Cookie': '_zap=661b9df6-8327-48a5-8b41-ae3b3089779a; _xsrf=p1XSVoTJkEXbFBXbKzT9EzX5jR35tEXh; d_c0="AJAim1vlCw-PTsW-nW-Wmk66OvrStYfapug=|1551276360"; capsion_ticket="2|1:0|10:1551276362|14:capsion_ticket|44:ODQ2OWFlNGJiYmE1NGU0ZDllMWU5NTY4NzIzNTczZjg=|91eef7ecd4c92d3ee9e1fc56d4d807764a279542a8552aef1b80b3fff38f08bd"; z_c0="2|1:0|10:1551276365|4:z_c0|92:Mi4xUDRmRUFnQUFBQUFBa0NLYlctVUxEeVlBQUFCZ0FsVk5UZWRqWFFDZkRKWUI3UkFjWUh4YzhmdmcxdGk4VVdhTXJ3|f2dc6bd10553ee7ff1c2e4162b2744fd9d5d0dbe6cf82dc07c4c7eb6ba010f8d"; tst=r; q_c1=4ff2802035d14ee5a6accaba8c214c93|1551276366000|1551276366000; tgw_l7_route=7c109f36fa4ce25acb5a9cf43b0b6415',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
r3 = requests.get('https://www.zhihu.com', headers=headers)
print(r3.text)
'''
# 会话维持
'''
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r4 = s.get('http://httpbin.org/cookies')
print(r4.text)
'''
# SSL证书验证
'''
import logging

logging.captureWarnings(True)  # 忽略警告
r5 = requests.get('https://www.12306.cn', verify=False)
print(r5.status_code)
'''
# 代理

# Prepared Request
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
