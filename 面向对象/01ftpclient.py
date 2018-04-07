#!/usr/bin/env python
# coding=utf-8

# 本来是想从aemy的ftpclient.py中导入aaron的ftpclient的一个类,发现导入不了有困难,待解决

from aaron.ftp_server import FtpServer

# 自省实现插程序槽式设计
# hasattr()
# getattr()
# setattr()
# delattr()


ftp_server = FtpServer('127.0.0.1')
if hasattr(ftp_server, 'put'):
    ftp_server.put()
else:
    print("put方法还没上线")
# connet 127.0.0.1
