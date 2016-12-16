#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
注意，如果类的成员变量与slots中的变量同名，
目前的实现是该变量被设置为readonly！！！
'''


class base(object):
    __slots__ = ('y',)

    y = 2
    v = 1

    def __init__(self):
        pass


b = base()
b.y = 3  # readonly
