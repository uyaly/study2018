
import socket
import threading
hostport = ('127.0.0.1',5560)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(hostport)
true = True
def Receve(s):
    global true
    while true:
        data = s.recv(1024).decode('utf8')
        if data == 'quit':
            true = False
        print('recevie news:\033[5;37;46m%s\033[0m' % data )
thrd=threading.Thread(target=Receve,args=(s,))
thrd.start()
while true:
    # user_input = input('>>>')
    user_input = '7E 02 00 40 55 01 00 00 00 00 01 38 01 80 42 79 00 4E 00 80 00 00 00 00 10 11 00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 08 23 10 55 28 01 04 00 01 2F 50 02 02 00 00 03 02 00 00 31 01 00 14 04 00 00 00 00 30 01 36 F0 01 03 F1 0A 30 8C AC 53 24 4F 18 00 74 8C F2 01 00 F3 02 03 63 F4 04 00 07 F1 FF E1 01 8B EC 7E'
    print(user_input)
    s.send(user_input.encode('utf8'))
    if user_input == 'quit':
        true = False
