#!/usr/bin/env python
#-*-coding:utf-8-*-

#每次处理一个字符串

def do_something(c):
    pass

def f_1(string):
    the_list = list(string)
    for c in the_list:
        do_something(c)

def f_2(string):
    return [do_something(c) for c in string]

def f_3(string):
    return map(do_something, string)