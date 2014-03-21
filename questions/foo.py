#!/usr/bin/env python
#-*-coding:utf-8-*-
res = []

def handle(numbers):
    current = 1
    while numbers > current:
        res.append(current)
        numbers -= current
        current += 1
    res.append(numbers)
    return res
print handle(11)
