#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent
import gevent.monkey
import time
import random

gevent.monkey.patch_all()


def foo(i_str):
    time.sleep(random.randint(1, 5))
    print i_str


tasks = [gevent.spawn(foo, str(i)) for i in range(0, 10)]
gevent.joinall(tasks)
