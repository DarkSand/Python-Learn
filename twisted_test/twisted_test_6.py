#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet import reactor, threads


def aSillyBlockingMethodOne(x):
    import time
    time.sleep(5)
    print x


def aSillyBlockingMethodTwo(x):
    import time
    time.sleep(1)
    print x


# run both methods sequentially in a thread
commands = [(aSillyBlockingMethodOne, ["Calling First"], {})]
commands.append((aSillyBlockingMethodTwo, ["And the second"], {}))
threads.callMultipleInThread(commands)
reactor.run()
