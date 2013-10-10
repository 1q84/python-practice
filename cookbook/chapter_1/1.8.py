#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
检查字符串是否包含某字符集和中的字符
"""

def contain(seq, aset):
    for c in seq:
        if c in aset:return True
    return False

import itertools
def contain_1(seq, aset):
    for item in itertools.ifilter(aset.__contains__, seq):
        return True
    return False

