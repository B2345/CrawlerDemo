# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File    : urllibTest.py
# @Author  : WSQ
# @Time    : 2019/3/2 20:41

# import urllib.request
# import urllib.error
from urllib import request, parse, error, robotparser
import socket

# 3.1.1 发送请求 urlopen, Request
## urlopen用法
'''
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))

try:
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
    response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=0.1)
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
'''

## Request用法
'''
request = urllib.request.Request('https://www.python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
'''

'''
url = 'http://httpbin.org/post'
# 1 添加headers的方式2
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'test'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# 2. 添加headers的方式2：add_header()
# req = request.Request(url=url, data=data,method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)');
req = request.Request(url, data, headers, 'POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
'''

# 3.1.2 处理异常 URLError
'''
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.URLError as e:
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
'''
# 3.1.3 解析链接 parse
'''
# urlparse
result = parse.urlparse('https://www.baidu.com/index.html;user?id=5#comment')
# result = parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(type(result), result, sep='\n')
# 提取域名
print(result.scheme, result[0], result.netloc, result[1], sep='\n')

# urlunparse
# urlparse() 对立方法 urlunparse()
data = ['http', 'www.baidu.con', 'index.html', 'user', 'a=5', 'comment']
unresult = parse.urlunparse(data)
print(unresult)  # 输出为：http://www.baidu.con/index.html;user?a=6#comment

# urlsplit 和 urlunsplit
splitResult = parse.urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(splitResult)

# urljoin
# 会分析 base_url 的 scheme、netloc、path 这三个内容对新链接缺失的部分进行补充，作为结果返回。

# urlencide 请求参数
params = {
    'name': 'test',
    'age': 22
}
base_url = 'https://www.baidu.com'
url = base_url + parse.urlencode(params)
print(url)
# 输出：https://www.baidu.comname=test&age=22

# parse_qs 和 parse_qsl
query = 'name=germey&age=22'
print(parse.parse_qs(query))  # 将参数转化为字典类
print(parse.parse_qsl(query))  # 将参数转化为元组组成的列表

# quote 和 unquote
# 将内容转化为 URL 编码的格式
keyword = '壁纸'
url = base_url + '/s?wd=' + parse.quote(keyword)
print(url)
# 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(parse.unquote(url))
'''

# 3.1.4  分析 Robots 协议（网络爬虫排除标准）
rp = robotparser.RobotFileParser('https://www.jianshu.com/robots.txt')
# 利用了 can_fetch() 方法来判断了网页是否可以被抓取。
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
