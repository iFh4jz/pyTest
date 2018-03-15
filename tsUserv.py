'''
这个脚本创建了一个UDP服务器，它接受
客户端发来的消息，并将加了时间戳前缀
的消息返回给客户端
'''

from socket import *
from time import ctime

HOST =''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print('...received from and returned to :', addr)
udpSerSock.close()