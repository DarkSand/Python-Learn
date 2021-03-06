#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    def __init__(self):
        self.attr = 'abc'


one = MyClass()
two = MyClass()

print one.attr
print two.attr

one.attr = 'cba'
print two.attr
