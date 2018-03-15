'''
通过使用SocketServer类、TCPServer和StreamRequestHandler,
该脚本创建了一个时间戳TCP服务器
'''

from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime