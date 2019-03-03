# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File    : RegExTest.py
# @Author  : WSQ
# @Time    : 2019/3/3 10:52

import re

"""
content1 = 'Hello 1234567 World_This is a Regex Demo'
print(len(content1))
result1 = re.match('^He.*?(\d+).*Demo$', content1)

print(result1)
print(result1.group())
print(result1.group(1))
print(result1.span())

content2 = 'http://weibo.com/comment/kEraCN'
result2 = re.match('http.*?comment/(.*?)', content2)
result3 = re.match('http.*?comment/(.*)', content2)
print('result2: ', result2.group(1))
print('result3: ', result3.group(1))


content3 = '''Hello 1234567 World_This
is a Regex Demo
'''
result3 = re.match('^He.*?(\d+).*?Demo$', content3, re.S)
print(result3.group(1))


content4 = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result4 = re.search('Hello.*?(\d+).*?Demo', content4)
print(result4.group())
print(result4.group(1))
"""

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''
html = re.sub('<a.*?>|</a>|<i.*?</i>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip())
