#!/usr/bin/env python
# coding=utf-8

# 高阶函数
# 1,参数是函数
# 2,返回值是函数

# 装饰器
# 1,不改变原函数代码
# 2,不改变原函数调用方法


# 参数是函数
def foo():
    print("foo is running")


def timer(func):
    print(func)  # <function foo at 0x00000000003B2E18>


timer(foo)


# 返回值是函数
def foo2():
    print("foo2 is running")


def timer2():
    return foo2


print(timer2())  # <function foo2 at 0x00000000026E8A60>
