#!/usr/bin/env python
# coding=utf-8

# 作用域: 变量逐层的网上找
name = "maotai" # <----------最后查

def f1():
    name = "maotai_f1" # <----------其次

    def f2():
        name = "maotai_f2"  # <----------首先
        print(name)
        # print(locals())
    f2()
f1()

# global


