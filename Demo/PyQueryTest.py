# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File    : PyQueryTest.py
# @Author  : WSQ
# @Time    : 2019/3/5 21:33

import requests
from pyquery import PyQuery

'''
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = PyQuery(html)
items = doc('.explore-tab .explore-feed').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = PyQuery(item.find('.content').text()).text()
    newline = '\n' + '=' * 50 + '\n'
    oneQuestion = '\n'.join([question, author, answer, newline])
    with open('zhihu.txt', 'a', encoding='utf-8') as file:
        file.write(oneQuestion)
'''


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    return html


def parse_one_page(html):
    doc = PyQuery(html)
    items = doc('.explore-tab .explore-feed').items()
    questions = ''
    for item in items:
        question = item.find('h2').text()
        author = item.find('.author-link-line').text()
        answer = PyQuery(item.find('.content').text()).text()
        newline = '\n' + '=' * 50 + '\n'
        oneQuestion = '\n'.join([question, author, answer, newline])
        questions = questions + oneQuestion
    return questions


def write_to_file(content):
    with open('zhihu.txt', 'a', encoding='utf-8') as file:
        file.write(content)


def main():
    url = 'https://www.zhihu.com/explore'
    html = get_one_page(url)
    content = parse_one_page(html)
    write_to_file(content)


if __name__ == '__main__':
    main()
