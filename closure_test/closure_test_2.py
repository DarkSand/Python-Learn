#!/usr/bin/env python
# -*- coding: utf-8 -*-


def hellocounter(name):
    count = [0]

    def counter():
        count[0] += 1
        print 'Hello,', name, ',', str(count[0]) + ' access!'

    return counter


hello = hellocounter('ma6174')
hello()
hello()
hello()
