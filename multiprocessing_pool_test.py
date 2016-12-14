#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import time
import random


def foo(i_str):
    time.sleep(random.randint(1, 5))
    print 'hello', i_str
    return i_str


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=10)

    result = []

    for i in xrange(0, 10):
        result.append(pool.apply_async(foo, (i,)))
    pool.close()
    pool.join()

    for res in result:
        print res.get()
