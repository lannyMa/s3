#!/usr/bin/env python
# coding=utf-8

def foo():
    print("foo is running")


def foo2():
    foo()
    print("foo2 is running")


foo2()

# foo is running
# foo2 is running
