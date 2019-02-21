# -*- coding: utf-8 -*-
import jenkins
import sys
import time
import json,urllib2

class jenkinsTest():

    #定义远程的jenkins master server的url，以及port
    jenkins_server_url='http://localhost:8080/'
    #定义用户的User Id 和 API Token，获取方式同上文
    user_id='admin'
    api_token='123456'
    job_name='dingding'
    def get_consoleinfo(self,jenkins_server_url, job_name, user_id, api_token):

        #实例化jenkins对象，连接远程的jenkins master server
        server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)

        #构建job名为job_name的job（不带构建参数）
        # server.build_job(job_name)
        #String参数化构建job名为job_name的job, 参数param_dict为字典形式，如：param_dict= {"param1"：“value1”， “param2”：“value2”}
        # server.build_job(job_name, parameters=param_dict)

        #获取job名为job_name的job的相关信息
        server.get_job_info(job_name)
        #获取job名为job_name的job的最后次构建号
        build_number = server.get_job_info(job_name)['lastBuild']['number']
        build_number = 514
        #获取job名为job_name的job的某次构建的执行结果状态
        build_result = server.get_build_info(job_name,build_number)['result']
        #判断job名为job_name的job的某次构建是否还在构建中
        server.get_build_info(job_name,build_number)['building']
        console_output = server.get_build_console_output(job_name,build_number)  # 控制台信息
        # 截取控制台信息msg
        start = console_output.find("***")
        if start >= 0:
            start += len("***")
            end = console_output.find("***", start)
            if end >= 0:
                msg = console_output[start:end].strip()
        return msg

    def run(self,jenkins_server_url, job_name, user_id, api_token):
        server = jenkins.Jenkins(url=jenkins_server_url, username=user_id, password=api_token)
        server.build_job(name=job_name, token=api_token)
        while True:
            time.sleep(1)
            print 'check running job...'
            if len(server.get_running_builds()) == 0:
                break
            else:
                time.sleep(20)
        last_build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
        build_info = server.get_build_info(job_name, last_build_number)
        build_result = build_info['result']
        print 'Build result is ' + build_result
        if build_result == 'SUCCESS':
            sys.exit(0)
        else:
            sys.exit(-1)

    def post(self):
def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)



if __name__ == '__main__':
