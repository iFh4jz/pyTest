'''
这是一个TCP服务器程序，它接受客户端发送的
数据字符串，并将其打上时间戳并返回给客户端
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from: ', addr)
    while True:
        data = tcpSerSock.recv(BUFSIZ).decode()
        if not data:
            break
        tcpSerSock.send('[%s] %s' % (ctime(), data).encode())
    tcpCliSock.close()
tcpSerSock.close()