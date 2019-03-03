# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File    : MaoYanTop100.py
# @Author  : WSQ
# @Time    : 2019/3/3 19:31

import requests
import re
import json
from requests.exceptions import RequestException
import time


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('MaoYanTop100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False))


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    items = parse_one_page(html)
    for item in items:
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=10 * i)
        time.sleep(1)
    print('success')

'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
for i in range(10):
    url = 'https://maoyan.com/board/4?offset=' + str(10 * i)
    req = requests.get(url=url, headers=headers)
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?name.*?href="(.*?)"\stitle="(.*?)"\s', re.S)
    results = re.findall(pattern, req.text)
    file = ''
    for result in results:
        file = file + result[0] + ' ' + result[2] + ' https://maoyan.com' + result[1] + '\n'
    with open('maoyaotop100.txt', 'a', encoding='utf-8') as f:
        f.write(file)
'''
