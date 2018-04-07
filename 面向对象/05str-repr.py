#!/usr/bin/env python
# coding=utf-8

class A:
    # def __str__(self):
    #     return "触发: __str__"

    def __repr__(self):
        return "触发: __repr__"

a = A()
print(a)