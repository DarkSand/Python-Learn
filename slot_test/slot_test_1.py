#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
python新模式的class，即从object继承下来的类有一个变量是__slots__，
slots的作用是阻止在实例化类时为实例分配dict，默认情况下每个类都会
有一个dict,通过__dict__访问，这个dict维护了这个实例的所有属性
'''


class base(object):
    v = 1

    def __init__(self):
        pass

    def adds(self, a, b):
        return a + b


b = base()
print b.__dict__

# 可以增加新的变量
b.x = 2
b.adds = lambda x, y: x - y
print b.__dict__
