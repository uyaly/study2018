import socket
hostname = '127.0.0.1'
port = 5566
addr = (hostname, port)
clientsock = socket.socket()
clientsock.connect(addr)
while True:
    data = input('>')
    if not data:
        break
    # say = input("666")
    clientsock.send(bytes(data, encoding='gbk'))
    recvdata = clientsock.recv(1024)
    if not recvdata:
        break
    print(recvdata)

clientsock.close()