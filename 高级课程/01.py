#!/usr/bin/env python
# coding=utf-8

class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.f1()

class Bar(Foo):
    def f1(self):
        print('Foo.f11111')


b=Bar()
b.f2()