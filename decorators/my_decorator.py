#!/usr/bin/env python
#-*-coding:utf-8-*-

def my_decorator(function):
    def _my_decorator(*args, **kw):
        #在调用实际函数之前做些填充工作
        res = function(*args, **kw)
        #做完某些填充工作之后
        return res
    #返回子函数
    return _my_decorator

def my_decorator(arg1, arg2):
    def _my_decorator(function):
        def __my_decorator(*args, **kw):
            res = function()
            return res
        return __my_decorator
    return _my_decorator

    