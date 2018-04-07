#!/usr/bin/env python
# coding=utf-8


class A:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        if self.x == 5:
            raise StopIteration("已到了5分")
        self.x += 1
        return self.x

a = A(1)

for i in a:
    print(i)
# 2
# 3
# 4
# 5
