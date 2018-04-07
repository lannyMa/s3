#!/usr/bin/env python
# coding=utf-8

import time


def foo():
    print("foo is running")


def timer(func):
    print(func)


timer(foo)
