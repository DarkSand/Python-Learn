#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
实例的dict只保持实例的变量，对于类的属性是不保存的，类的属性
包括变量和函数。由于每次实例化一个类都要分配一个新的dict，因
此存在空间的浪费，因此有了slots，当定义了slots后，slots中定
义的变量变成了类的描述符，相当于java，c++中的成员变量声明，
类的实例只能拥有这些个变量，而不在有dict，因此也就不能在增加
新的变量
'''


class base(object):
    __slots__ = ('y',)
    v = 1

    def __init__(self):
        pass


b = base()

# // error, 不能增加新的变量(任何试图创建一个其名不在__slots__中的名字的实例属性都将导致AttributeError异常)
b.x = 2
