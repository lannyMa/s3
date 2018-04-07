#!/usr/bin/env python
# coding=utf-8


## 函数的作用域跟函数在哪定义有关,和在哪调用该函数无关
name = "maotai"
def f1():
    def f2():
        name = "maotai_f2"
        def f3():
            print(name)
        return f3
    return f2


f1()()()  # maotai_f2

