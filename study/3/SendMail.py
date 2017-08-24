# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.text import MIMENonMultipart

# ----------1.跟发件相关的参数------
smtpserver = "smtp.126.com"             # 发件服务器
port = 0                                # 端口
sender = "uuyaly@126.com"                 # 账号
psw = "612101010"                  # 密码
receiver = "uuuyaly@qq.com"           # 接收人
# ----------2.编辑邮件的内容------
subject = "这个是主题"
body = '<p>这个是自动发送的邮件</p>'     # 定义邮件正文为html格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "uuuyaly@qq.com"
msg['subject'] = subject
# ----------3.发送邮件------
# 为了兼容qq邮箱的SSL
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)                # 连服务器
    smtp.login(sender, psw)                 # 登录
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)                 # 登录

smtp.sendmail(sender, receiver, msg.as_string())    # 发送
smtp.quit()                             # 关闭
# 授权码 qq（uuu）邮箱密码 kjhpjigpcglmbgde