#!/usr/bin/env python
#-*-coding:utf-8-*-
import re

def reverse(s):
    p = re.compile(r'\w+')
    for m in p.finditer(s):
        word = m.group()
        if word:
            p = s.partition(word)
            l = list(p)
            index = p.index(word)
            l[index] = l[index][::-1]
            l2 = list(l[index])
            l2[0],l2[-1]=l2[-1],l2[0]
            l[index]=''.join(l2)
            s = ''.join(l)
    return s

s=" Alistair Chris, "
print "%s" % reverse(s)