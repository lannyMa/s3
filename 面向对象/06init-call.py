#!/usr/bin/env python
# coding=utf-8

class A:
    def __init__(self):
        print("触发 __init__")

    def __call__(self):
        print("触发 __call__")

a = A()
a()