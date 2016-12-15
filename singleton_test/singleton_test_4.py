#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Singleton, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass(Singleton):
    def __init__(self):
        self.attr = 'abc'


one = MyClass()
two = MyClass()

print one.attr
print two.attr

one.attr = 'cba'
print two.attr
