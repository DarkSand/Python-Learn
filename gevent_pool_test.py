#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent
import gevent.monkey
from gevent.pool import Pool
import random
import time

gevent.monkey.patch_all()


def foo(i_str):
    time.sleep(random.randint(1, 5))
    print i_str


pool = Pool(10)

pool.map(foo, range(0, 10))
