#!/usr/bin/env python
# coding=utf-8

# 只允许属性设置str类型value
class A:
    def __setattr__(self, key, value):
        if type(value) is str:
            self.__dict__[key] = value
            print("%s = '%s'" % (key, value))
        else:
            print("value只允许为str类型")


# a = A()
# a.name = "maotai"
# a.age = 22

# 列表只能append str类型
class my_list(list):

    def append(self, value):
        res = []
        if type(value) is str:
            # res.append(value)
            super().append(value)
        else:
            print("设置失败: value只允许str类型")
        return res


# arr = my_list()
# arr.append('mao')
# arr.append('tai')
# arr.append(22)  # 设置失败: value只允许str类型
# print(arr)  # ['mao', 'tai']


# 求列表中间值
class list_mid(list):
    def mid(self):
        return self[int(len(self) / 2)]


# arr = list_mid()
# arr.append(1)
# arr.append(2)
# arr.append(3)
# print(arr.mid())

# 另一个思路: self
# 写文件带时间

import time


class Open:
    def __init__(self, filename, mode, encoding):
        # self.filename = filename
        self.file = open(filename, mode=mode, encoding=encoding)
        self.mode = mode
        self.encoding = encoding

    def write(self, content):
        t = time.strftime("%Y-%m-%d %X")
        self.file.write("%s: %s\n" % (t, content))  # <--------关键在于这里
        # self.close()

    def __getattr__(self, item):
        print("触发__getattr__:", item)


f = Open("test.txt", 'w', 'utf8')
f.write("cpu不足")
f.write("内存不足")
f.write("磁盘不足")
