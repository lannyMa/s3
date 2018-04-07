#!/usr/bin/env python
# coding=utf-8
import time


def timer(func):
    def wrapper():
        s = time.time()
        res = func()
        e = time.time()
        print("运行时间: ", e - s)
        return res

    return wrapper


@timer
def test():
    time.sleep(1)
    print("test is running")
    return "maotai"

res = test() #运行test就是在运行wrapper,
print(res)
# test is running
# 运行时间:  1.0000572204589844
# maotai



a = str("ma")