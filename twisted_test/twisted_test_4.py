#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet import reactor


def f():
    print "I'll never run."


callID = reactor.callLater(5, f)
callID.cancel()
reactor.run()
