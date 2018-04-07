#!/usr/bin/env python
# coding=utf-8

py_class = ['wang', 'zhang', 'zhou']
linux_class = ['wang', 'zhou']

# py_and_linux = []
# for i in py_class:
#     if i in linux_class:
#         py_and_linux.append(i)
# print(py_and_linux)  # ['wang', 'zhou']

print(set(py_class + linux_class))  # arr去重

py_class_s = set(['wang', 'zhang', 'zhou'])
linux_class_s = set(['wang', 'zhou'])

## 交集
print("交集s1 & s2", py_class_s & linux_class_s)  # 交集s1 & s2 {'zhou', 'wang'}
print("交集s1.intersection(s2)", py_class_s.intersection(linux_class_s))  # 交集s1.intersection(s2) {'zhou', 'wang'}

## 并集
print("并集: s1 | s2 ", py_class_s | linux_class_s)  # 并集: s1 | s2  {'zhou', 'zhang', 'wang'}
print("并集: s1.union(2) ", py_class_s.union(linux_class_s))  # 并集: s1.union(2)  {'zhou', 'zhang', 'wang'}

## 差集
py_class_s = set(['wang', 'zhang', 'zhou'])
linux_class_s = set(['wang', 'zhou'])

print("差集: s1 - s2", py_class_s - linux_class_s)  # {'zhang'}
print("差集: s1.difference(s2)", py_class_s.difference(linux_class_s))  # {'zhang'}
