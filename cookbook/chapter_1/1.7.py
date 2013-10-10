#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
将字符串逐字符或逐词反转
"""

def reverse(string):
    return string[::-1]

def reverse_2(string):
    return ' '.join(string.split()[::-1])

print reverse('haha hei')
print reverse_2('haha hei')