#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet import reactor
import time


def notThreadSafe(x):
    """do something that isn't thread-safe"""
    # ...
    time.sleep(3)
    print 'do something not safe', x


def threadSafeScheduler():
    """Run in thread-safe manner."""
    reactor.callFromThread(notThreadSafe, 1)  # will run 'notThreadSafe(3)'
    reactor.callFromThread(notThreadSafe, 2)
    reactor.callFromThread(notThreadSafe, 3)
    reactor.callFromThread(notThreadSafe, 4)
    reactor.callFromThread(notThreadSafe, 5)


threadSafeScheduler()
reactor.run()
