# -*- coding: utf-8 -*-
import jenkins
import sys
import time
import reply

class jenkinsinfo(object):

    def __init__(self, user_name):
        #定义远程的jenkins master server的url，以及port
        self.jenkins_server_url='http://localhost:8080/'
        #定义用户的User Id 和 API Token，获取方式同上文
        self.user_id='admin'
        self.api_token='123456'
        self.job_name='dingding'
        self.server = jenkins(self.jenkins_server_url, self.user_id, self.api_token)
        self.user_name = user_name

    def run(self):
        self.server.build_job(self.job_name, self.api_token)
        while True:
            time.sleep(1)
            print 'check running job...'
            if len(self.server.get_running_builds()) == 0:
                break
            else:
                time.sleep(20)
        last_build_number = self.lastnumber()
        build_info = self.server.get_build_info(self.job_name, last_build_number)
        build_result = build_info['result']
        print 'Build result is ' + build_result
        if build_result == 'SUCCESS':
            sys.exit(0)
        else:
            sys.exit(-1)
        return last_build_number

    def lastnumber(self):
        last_build_number = self.server.get_job_info(self.job_name)['lastCompletedBuild']['number']
        return last_build_number

    def consoleinfo(self, build_number):
        console_info = self.server.get_build_console_output(self.job_name, build_number)  # 控制台信息
        # 截取控制台信息msg
        start = console_info.find("***")
        if start >= 0:
            start += len("***")
            end = console_info.find("***", start)
            if end >= 0:
                msg = console_info[start:end].strip()
        print "last msg:", msg
        return msg

    def sendinfo(self):
        try:
            recMsg = self.consoleinfo()
            if(self.user_name == "U"):
                toUser = "oyJXO07T6RM7v610Bzd2Zxlv3Vz8" # U:oyJXO07T6RM7v610Bzd2Zxlv3Vz8
            elif(self.user_name == "Y"):
                toUser = "oyJXO03XskpUoHyh8PY1pYmI0xmY" # U:oyJXO03XskpUoHyh8PY1pYmI0xmY
            else:
                pass

            fromUser = "gh_0c619267e79e"

            reply1 = reply.TextMsg(toUser, fromUser, recMsg)
            return reply1.send()  #
        except Exception, Argment:
            return Argment

if __name__ == '__main__':
    j = jenkinsinfo("U")
    r = j.sendinfo()
    print(r)
