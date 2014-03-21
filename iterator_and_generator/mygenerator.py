#!/usr/bin/env python
#-*-coding:utf-8-*-

def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print "ok let's clean"

gen = my_generator()
print gen.next()
print gen.throw(ValueError('mean mean mean'))
gen.close()
print gen.next()

