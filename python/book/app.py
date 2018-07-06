# encoding:UTF-8
from readlist import ScanFile
from flask import Flask,render_template,request,make_response
import hashlib
import hashlib
import time
import os
import urllib2,json


app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return render_template('home.html')

# @app.route('/form', methods=['GET'])
# def signin_form():
#     return render_template('form.html')

# @app.route('/signin', methods=['POST'])
# def signin():
#     username = request.form['username']
#     password = request.form['password']
#     if username=='admin' and password=='password':
#         return render_template('signin-ok.html', username=username)
#     return render_template('form.html', message='Bad username or password', username=username)


@app.route("/",methods = ["GET","POST"])
def wechat_auth():
    if request.method == 'GET':
        if len(request.args) > 3:
            token = 'wechat'
            query = request.args
            signature = query['signature']
            timestamp = query['timestamp']
            nonce = query['nonce']
            echostr = query['echostr']
            s = [timestamp, nonce, token]
            s.sort()
            s = ''.join(s)
            sha1str = hashlib.sha1(s).hexdigest()
            if sha1str == signature:
                return make_response(echostr)
            else:
                return make_response("认证失败")
        else:
            return "认证失败"

def POST(self):
        str_xml = request.data() #获得post来的数据
        # xml = etree.fromstring(str_xml)#进行XML解析
        content=str_xml.find("Content").text#获得用户所输入的内容
        msgType=str_xml.find("MsgType").text
        fromUser=str_xml.find("FromUserName").text
        toUser=str_xml.find("ToUserName").text
        return self.render.reply_text(fromUser,toUser,int(time.time()),u"我现在还在开发中，还没有什么功能，您刚才说的是："+content)

@app.route('/book', methods=['GET'])
def booklist():
    dir = './static/'     #需要扫描的文件路径
    scan = ScanFile(dir, postfix=".py")
    subdirs = scan.scan_subdir()   # 文件夹路径
    files = scan.scan_files()     # 文件
    namedirs = []
    for i in range(len(subdirs)):
        name = subdirs[i]
        lenth = len(subdirs[i])
        namedirs.append(name[9:lenth])
    return render_template('home.html',lenth = len(subdirs), namelist=namedirs)

    # print u"扫描的子目录是:"
    # for subdir in subdirs:
    #     print namedirs.decode('gbk').encode('utf-8')
@app.route('/book/<name>', methods=['GET'])
def book_name(name):
    # return render_template('static.html?name= %s' % name)
    return render_template('book.html', name=name)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80, debug=True)