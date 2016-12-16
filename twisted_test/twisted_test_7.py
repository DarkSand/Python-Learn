#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet import reactor, threads


def doLongCalculation():
    # .... do long calculation here ...
    return 3


def printResult(x):
    print x


# run method in thread and get result as defer.Deferred
d = threads.deferToThread(doLongCalculation)
d.addCallback(printResult)
reactor.run()
