#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet import threads, reactor, defer
from twisted.web.client import getPage
from twisted.web.error import Error

# 修改线程池大小
reactor.suggestThreadPoolSize(30)


def inThread():
    try:
        result = threads.blockingCallFromThread(reactor, getPage, "http://www.jd.com/")
    except Error, exc:
        print exc
    else:
        print result
    reactor.callFromThread(reactor.stop)


reactor.callInThread(inThread)
reactor.run()
