#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
装饰器就是一种闭包
"""


def makebold(fn):
    def wrapped():
        return "<bold>" + fn() + "</bold>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<italic>" + fn() + "</italic>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


print hello()
