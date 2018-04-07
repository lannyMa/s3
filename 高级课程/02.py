#!/usr/bin/env python
# coding=utf-8

class A:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("A show")


class B(A):
    pass


b = B("maotai")
print(b.name)  # maotai
b.show()  # A show


def show():
    n = 0
    if n > 10:
        print("hello world")
        show()
        n += 1
show()
