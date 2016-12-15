#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton(object):
    def __init__(self):
        self.attr = 'abc'

    def foo(self):
        print self.attr


my_singleton = Singleton()
