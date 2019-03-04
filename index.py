# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File    : index.py
# @Author  : WSQ
# @Time    : 2019/3/2 12:07


def fun():
    for i in range(20):
        x = yield i
        print('good', x)


if __name__ == '__main__':
    a = fun()
    a.__next__()
    x = a.send(5)
    print(x)
