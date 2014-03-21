#!/usr/bin/env python
#-*-coding:utf-8-*-

import time
import hashlib
import pickle

cache = {}
def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration

def computer_key(function, args, kw):
    key = pickle.dumps((function.func_name, args, kw))
    return hashlib.sha1(key).hexdigest()

def memoize(duration=30):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = computer_key(function, args, kw)
            if key in cache and not is_obsolete(cache[key], duration):
                print 'wo got a winner'
                return cache[key]['value']
            result = function(*args, **kw)
            cache[key] = {'value':result,'time':time.time()}
            return result
        return __memoize
    return _memoize

@memoize()
def very_complex_stuff(a,b):
    return a + b

very_complex_stuff(2,2)

