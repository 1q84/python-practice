#!/usr/bin/env python
#-*-coding:utf-8-*-

def fibonacci():
    a, b = 0, 1
    while  True:
        yield b
        a, b = b, a + b

fib = fibonacci()
print [fib.next() for i in range(10)]
print map(lambda x,f = lambda x,f:f(x-1,f)+f(x-2,f) if x >1 else x:f(x,f),range(10))
