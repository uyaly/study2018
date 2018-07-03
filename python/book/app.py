# encoding:UTF-8
from readlist import ScanFile
from flask import Flask, render_template

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

@app.route('/', methods=['GET'])
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
@app.route('/<name>', methods=['GET'])
def book_name(name):
    # return render_template('static.html?name= %s' % name)
    return render_template('book_app.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, debug=True)