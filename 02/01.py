#!/usr/bin/env python
# coding=utf-8

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('192.168.1.101', 8001))

phone.send("hello".encode("utf-8"))
data = phone.recv(1024)
print("收到服务端发来的消息: ", data)
