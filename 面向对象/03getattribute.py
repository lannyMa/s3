#!/usr/bin/env python
# coding=utf-8

class A:
    age = 22
    def __getattribute__(self, item):
        print("触发: __getattribute__")
        raise AttributeError
    def __getattr__(self, item):
        print("触发: __getattr__")

# 对类不起作用

#
a = A()
a.name # 获取属性(不存在): 触发: __getattribute__
       # 获取属性(不存在): 触发: __getattr__
a.age # 获取属性(存在): 触发: __getattribute__
       # 获取属性(存在): 触发: __getattr__
