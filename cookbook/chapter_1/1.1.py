#!/usr/bin/env python
#-*-coding:utf-8-*-
#判断一个对象是否是字符串

def is_string(obj):
    return isinstance(obj,str)

def is_string_2(obj):
    import types
    return obj is types.StringType()


obj=''
print is_string(obj)
print is_string_2(obj)