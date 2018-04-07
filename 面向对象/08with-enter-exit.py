#!/usr/bin/env python
# coding=utf-8

# 追踪信息+异常类+异常值
# raise AttributeError("hello world")


class Open:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("触发: __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("触发: __exit__")


# with Open('1.txt') as f:
#     print("======>")
# 触发: __enter__
# ======>
# 触发: __exit__


class Open2:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("触发: __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("触发: __exit__")
        print("exc_type:", exc_type)
        print("exc_val:", exc_val)
        print("exc_tb:", exc_tb)


# with Open2('1.txt') as f:
#     print("=======>")

# 触发: __enter__
# =======>
# 触发: __exit__
# exc_type: None
# exc_val: None
# exc_tb: None


class Open3:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("触发: __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("触发: __exit__")
        print("exc_type:", exc_type)
        print("exc_val:", exc_val)
        print("exc_tb:", exc_tb)


# with Open3('1.txt') as f:
#     print("=======>")
#     raise AttributeError("属性不存在")

# 触发: __enter__
# =======>
# 触发: __exit__
# exc_type: <class 'AttributeError'>
# exc_val: 属性不存在
# exc_tb: <traceback object at 0x00000000021DBF08>
# Traceback (most recent call last):
#   File "C:/Users/Administrator/PycharmProjects/s3/面向对象/08with-enter-exit.py", line 67, in <module>
#     raise AttributeError("属性不存在")
# AttributeError: 属性不存在

class Open4:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("触发: __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("触发: __exit__")
        print("exc_type:", exc_type)



# with Open4('1.txt') as f:
#     print("=======>")
#     raise AttributeError("属性不存在")
#
# print("执行跟with语句无关的代码..")

# 触发: __enter__
# Traceback (most recent call last):
# =======>
#   File "C:/Users/Administrator/PycharmProjects/s3/面向对象/08with-enter-exit.py", line 95, in <module>
# 触发: __exit__
#     raise AttributeError("属性不存在")
# AttributeError: 属性不存在
# exc_type: <class 'AttributeError'>



class Open5:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("触发: __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("触发: __exit__")
        print("exc_type:", exc_type)
        return True


# with Open5('1.txt') as f:
#     print("=======>")
#     raise AttributeError("属性不存在")
#
# print("执行跟with语句无关的代码..")

# 触发: __enter__
# =======>
# 触发: __exit__
# exc_type: <class 'AttributeError'>
# 执行跟with语句无关的代码..