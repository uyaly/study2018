# -*- coding: utf-8 -*-
import jenkins
import re
import sys
import time

#定义远程的jenkins master server的url，以及port
jenkins_server_url='http://localhost:8080/'
#定义用户的User Id 和 API Token，获取方式同上文
user_id='admin'
api_token='123456'
job_name='dingding'
# def info(self,jenkins_server_url, job_name, user_id, api_token):

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
print msg