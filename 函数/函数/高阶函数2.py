#!/usr/bin/env python
# coding=utf-8

# 参数为函数,实现函数运行计时功能
import time


def foo():
    print("foo is running")


def timer(func):
    s = time.time()
    func()
    time.sleep(1)
    e = time.time()
    # print(e - s)
    return func
foo = timer(foo)
foo()

# foo is running
# 1.0000572204589844

# 实现不改变原函数调用方法
def foo2():
    print("foo2 is running")


def timer2():
    return foo2


foo2 = timer2()
foo2()
# foo2 is running
