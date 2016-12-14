#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import time
import random


def foo(i_str):
    time.sleep(random.randint(1, 5))
    print i_str


if __name__ == '__main__':
    tasks = [multiprocessing.Process(target=foo, args=(i,)) for i in range(0, 10)]
    for task in tasks:
        task.start()
