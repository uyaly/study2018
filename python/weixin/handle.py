# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import web
import receive
import reply
import Robot


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "wechat2019" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            # print "Handle Post webdata is ", webData  #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                recriveMsg = recMsg.Content
                # print "Handle receive:", recriveMsg
                replyMsg = Robot.RobotQYK().content(recriveMsg)  #  机器人
                # print "Handle reply:",(replyMsg)
                reply1 = reply.TextMsg(toUser, fromUser, replyMsg)
                return reply1.send()  # 重复你说的

            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment


    def POST(self, action, recMsg):
        try:
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.ToUserName
                fromUser = recMsg.FromUserName
                recriveMsg = recMsg.content
                print "Handle receive:", recriveMsg
                reply1 = reply.TextMsg(toUser, fromUser, recriveMsg)
                return reply1.send()  # 重复你说的

            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment