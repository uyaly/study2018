# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----------1.跟发件相关的参数------
smtpserver = "smtp.126.com"             # 发件服务器
port = 0                                # 端口
sender = "uuyaly@126.com"                 # 账号
psw = "612101010"                  # 密码
receiver = ["uuuyaly@qq.com", "uuyaly@qq.com"]           # 接收人
subject = "这个是主题"
# body = '<p>这个是自动发送的邮件</p>'     # 定义邮件正文为html格式

# ----------2.编辑邮件的内容------
# 读文件
file_path = r"D:\PycharmProjects\test\lytest\report\result.html"
with open(file_path, "rb")as fp:
    mail_body = fp.read()
    msg = MIMEMultipart()
    msg['from'] = sender
    msg['to'] = ";".join(receiver)      # 多收件人list转str
    msg['subject'] = subject
    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="test_report.html"'
    msg.attach(att)
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
