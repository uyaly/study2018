# coding:utf-8
from flask import Flask, session, redirect, url_for, escape, request


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # 使用 Jinja 模板，只需要使用render_template函数并传入模板文件名和参数名即可。
    return render_template('hello.html', name=name)

# 日志
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')



if __name__ == '__main__':
    app.run()