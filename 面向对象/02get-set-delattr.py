#!/usr/bin/env python
# coding=utf-8

class A:
    name = "maotai"

    def __getattr__(self, item):
        print("触发__getattr__")

    def __delattr__(self, item):
        print("触发: __delattr__")

    def __setattr__(self, instance, value):
        print("触发: __setattr__")


# 对于类没啥卵用
# A.names         # 获取类属性(不会触发), AttributeError: type object 'A' has no attribute 'names'
# del A.name      # 删除类属性(不会触发)
# A.gender="male" # 增加类属性(不会触发)

a = A()
a.name  # 获取属性: 属性存在时,不会触发__getattr__
a.names  # 获取属性: 属性不存在时,会触发__getattr__

del a.name  # 删除属性: 属性存在,会触发: __delattr__
del a.names  # 删除属性: 属性不存在,会触发: __delattr__

a.age = 22  # 增加属性触发: __setattr__


# ___init__也会触发...
class Open:
    def __init__(self, filename, mode, encoding):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __setattr__(self, key, value):
        print("%s: 触发__setattr__" % key)


f = Open("test.txt", 'r', 'utf8')
# filename: 触发__setattr__
# mode: 触发__setattr__
# encoding: 触发__setattr__
