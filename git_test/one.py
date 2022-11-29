# -*- coding:utf-8 -*-
# author：LJ
# 日期：2022年11月28日
# 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
import requests
import sys

def sys_get():
    print(sys.argv)

def mast():
    a = 5
    b = 5
    print(a + b)
    response = requests.get("https://www.baidu.com")
    print(response.text)


if __name__ == '__main__':
    print("hello world!")
    print("kgithub")
    mast()
