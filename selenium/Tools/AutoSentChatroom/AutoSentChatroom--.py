# coding:UTF-8
import itchat, time
from itchat.content import *
def lc():
    print("Finash Login!")
def ec():
    print("exit")
# 登录
itchat.auto_login(loginCallback=lc, exitCallback=ec)

# 发送消息send(msg="Text Message", toUserName=None)
itchat.send("Hello World!")
# itchat.send("@fil@%s" % '/tmp/test.txt')
# itchat.send("@img@%s" % '/tmp/test.png')
# itchat.send("@vid@%s" % '/tmp/test.mkv')
itchat.send("@vid@%s" % '/tmp/test.mkv')

# 下载附件
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    # msg.download(msg['FileName'])   # 这个同样是下载文件的方式
    msg['Text'](msg['FileName'])      # 下载文件
    # 将下载的文件发送给发送者
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg["FileName"]), msg["FromUserName"])

itchat.logout()    #  强制退出登录

