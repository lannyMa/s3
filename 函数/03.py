#!/usr/bin/env python
# coding=utf-8
import time


def foo():
    time.sleep(1)
    print("show is running")


def timer(func):
    stime = time.time()
    func()
    etime = time.time()
    print(etime - stime)


timer(foo)

# show is running
# 1.0000572204589844
