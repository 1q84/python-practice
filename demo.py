#!/usr/bin/env python
#-*-coding:utf-8-*-

class A():

    def foo(self):
        return 'A'

    def bar(self):
        return 'B'

class B(A):

    def foo(self):
        return 'C'

    def bar(self):
        return 'D'

if __name__ == "__main__":
    b = B()
    print b.foo()
