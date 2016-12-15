#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
闭包就是根据不同的配置信息得到不同的结果
addend 就是配置信息
虽然p和q都是make_adder生成的,但是因为配置参数不同,后面再执行相同参数的函数后得到了不同的结果.这就是闭包

创建一个闭包必须满足以下几点:
1.必须有一个内嵌函数
2.内嵌函数必须引用外部函数中的变量
3.外部函数的返回值必须是内嵌函数
"""


def make_adder(addend):
    def adder(augend):
        return augend + addend

    return adder


p = make_adder(23)
q = make_adder(44)

print p(100)
print q(100)
