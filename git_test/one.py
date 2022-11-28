# -*- coding:utf-8 -*-
# author：LJ
# 日期：2022年11月28日

import requests

def mast():
    a = 5
    b = 5
    print(a+b)
    response = requests.get("www.baidu.com")
    print(response.text)

if __name__ == '__main__':
    print("hello world!")
    mast()
