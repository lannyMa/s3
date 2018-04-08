#!/usr/bin/env python
# coding=utf-8

age = 22

# 函数内对全局变量默认只读权限
## 例子1
def f1():
    print(age)


f1()  # 22
print(age)  # 22

## 例子2
def f2():
    age = 23
    print(age)


f2()  # 23
print(age)  # 22

# 函数内对全局变量(不可变类型)+global 读写权限
def f3():
    global age
    age = 10
    print(age)
f3()       # 10
print(age) # 10

#  函数内对全局变量(可变类型)默认: 读写权限
arr = [1,2,3]
def f4():
    arr.append(4)
    print(arr)
f4() # [1, 2, 3, 4]
print(arr) # [1, 2, 3, 4]