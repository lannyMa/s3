#!/usr/bin/env python
# coding=utf-8


def father(name):
    name = "maotai_2"

    def son():
        name = "maotai_3"
        print("son: i am %s" % name)

        def grandson():
            name = "maotai_4"
            print("grandson: i am %s" % name)
        grandson()
    son()

father("maotai")

# son: i am maotai_3
# grandson: i am maotai_4