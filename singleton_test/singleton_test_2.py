#!/usr/bin/env python
# -*- coding: utf-8 -*-


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class MyClass(object):
    def __init__(self):
        self.attr = 'abc'

one = MyClass()
two = MyClass()

print one.attr
print two.attr

one.attr = 'cba'
print two.attr
