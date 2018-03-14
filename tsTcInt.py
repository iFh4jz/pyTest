'''
这个脚本创建一个TCP客户端，它提示用户输入发送到服务器端的消息
并接收从服务器端返回的添加了时间戳前缀的相同消息，然后将结果显示

'''
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()