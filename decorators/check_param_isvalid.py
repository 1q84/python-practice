#!/usr/bin/env python
#-*-coding:utf-8-*-
def check_param_isvalid():
    def check(method):
        def check_param(*args,**kwargs):
            for a in args:
                assert isinstance(a, int),"arg %r does not match %s" % (a,int)
                assert a > 100000,"arg %r must gt 100000" % a
            return method(*args, **kwargs)
        return check_param
    return check

@check_param_isvalid()
def foo(*args):
    print args

foo(200000,500000)