#!/usr/bin/env python
# coding=utf-8

class A:
    name = "maotai"

    def __getitem__(self, item):
        print("触发: __getitem__")

    def __setitem__(self, key, value):
        print("触发: __setitem__")

    def __delitem__(self, key):
        print("触发: __delitem__")


# 对于类不起作用
# A.name
# A.names # AttributeError: type object 'A' has no attribute 'names'
# A['name']  # TypeError: 'type' object is not subscriptable

# 对于实例
a = A()
a['name']  # 获取属性(存在): 触发: __getitem__
a['names']  # 获取属性(不存在): 触发: __getitem__

a['name'] = "maotai"  # 设置属性: 触发: __setitem__
a['name'] = "maotai2"  # 修改属性: 触发: __setitem__
del a['name']  # 删除属性(存在): 触发: __delitem__
del a['age']  # 删除属性(不存在): 触发: __delitem__
