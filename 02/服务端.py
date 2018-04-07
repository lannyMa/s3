#!/usr/bin/env python
# coding=utf-8

import socket

# 使用AF_INET家族 tcp
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买手机

phone.bind(("192.168.1.101", 8001))  # 绑定手机卡

phone.listen(5)  # 开机

conn, addr = phone.accept()  # 等电话
msg = conn.recv(1024)  # 收信息
conn.send(msg.upper())  # 发信息

print("客户端发来的消息是", msg)

conn.close()  # 挂电话
phone.close()  # 关机
