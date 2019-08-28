import datetime
import socket
import threading
flag = False

class conn:

    def Receve(self,s):
        global flag
        while flag:
            data = s.recv(1024).decode('utf8')
            if data == 'quit':
                flag = False
            print('recevie news:%s' % data)
            # self.textEdit_log.insertPlainText(self.T)
            # self.textEdit_log.insertPlainText(data)

    def __init__(self):
        global flag
        flag = bool(1 - flag)  # flag取反
        print(flag)
        hostport = ('127.0.0.1',5560)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threads = []
        t1 = threading.Thread(self.Receve(s))   # 接收信息
        threads.append(t1)
        # t2 = threading.Thread(target=resultlist)  # 显示结果
        # threads.append(t2)
        for t in threads:
            if flag:
                s.connect(hostport)
                t.setDaemon(True)
                t.start()
            else:
                t.join()
                s.close()


    def sendmsg(self, s):
        global flag
        while flag:
            send_msg = self.textEdit.toPlainText()
            if send_msg == '':
                break
            else:
                s.send(bytes(send_msg, encoding='gbk'))
                # T = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # self.textEdit_log.insertPlainText(T)
                # self.textEdit_log.insertPlainText(send_msg)
            if send_msg == 'quit':
                flag = False

if __name__ == '__main__':
    conn
