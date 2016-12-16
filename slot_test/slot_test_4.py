#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Python 是一门动态语言，可以在运行过程中，修改对象的属性和增删方法。任何类
的实例对象包含一个字典__dict__, Python通过这个字典将任意属性绑定到对象上。
有时候我们只想使用固定的对象，而不想任意绑定对象，这时候我们可以定义一个
属性名称集合，只有在这个集合里的名称才可以绑定。__slots__就是完成这个功能
的。

一个类里面，如果定义了__slot__，则对象里面就没有了__dict__
这样就不能任意绑定属性，只能绑定__slots__属性名称集合里的同名属性了。
'''


class test(object):
    # 可以访问foo
    __slots__ = ('foo');
    foo = 1.3


a = test()
print a.foo
a.bar = 15
print a.bar
