#!/usr/bin/env python
# coding=utf-8

import sys

sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\s3\\面向对象\\aaron')
from aaron.server import FtpServer

class A:
    ftp = FtpServer('192.168.1.2')
