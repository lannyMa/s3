#!/usr/bin/env python
# coding=utf-8


arr = [1, 2, 3, 4, 5]

from functools import reduce

print(reduce(lambda x, y: x * y, arr))  # 120
print(reduce(lambda x, y: x * y, arr, 10))  # 1200,加基数10
