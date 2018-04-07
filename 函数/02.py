#!/usr/bin/env python
# coding=utf-8

def foo():
    print("foo is running")


def timer(func):
    return func

foo = timer(foo)
foo()  # 执行foo, 以前的执行方式没变
