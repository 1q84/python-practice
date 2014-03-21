#!/usr/bin/env python
#-*-coding:utf-8-*-

def grapes(x):

   return x*x*x

def apples(n, f):
    y = 0
    for i in range (1, n + 1):
        y = y + f(i)
    return y

n = 3
f = grapes

print f(1)+f(2)+f(3)

print("apples(%s, %s) = %s, %s" %(n, f, apples(n, f), "PASS" if apples(n, f) == 32 else "FAIL"))