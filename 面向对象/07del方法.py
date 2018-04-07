#!/usr/bin/env python
# coding=utf-8

class A:
    def __del__(self):
        print("触发: __del__")

a = A()
# del a
print('---->')