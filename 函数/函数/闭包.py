#!/usr/bin/env python
# coding=utf-8


def foo():
    name = "maotai"

    def f2():
        age = 22

    print(locals())


foo()  # {'f2': <function foo.<locals>.f2 at 0x00000000022189D8>, 'name': 'maotai'}
