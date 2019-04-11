#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import getweb as gw
from Tkinter import *
import webbrowser
import time
reload(sys)
sys.setdefaultencoding( "utf-8" )
#窗口
window = Tk()
window.title('定时获取')
window.geometry('580x650')
# 左侧题目数量
frame_left = LabelFrame(window, text="地  址", labelanchor="n")
frame_left.place(relx=0.02, rely=0, relwidth=0.52, relheight=0.2)

Label(frame_left,text='网址：').place(relx=0.02, rely=0.02)
v_url=StringVar()
Entry(frame_left,textvariable=v_url, width=35).place(relx=0.12, rely=0.02)
v_url.set('http://www.deyi.com/forum-23-1.html')

# 右侧配置区
frame_right = LabelFrame(window, text="配  置", labelanchor="n")
frame_right.place(relx=0.55, rely=0, relwidth=0.4, relheight=0.2)

Label(frame_right,text='间隔时间（秒）:').place(relx=0.02, rely=0.02)
Label(frame_right,text='关键字:').place(relx=0.02, rely=0.22)
# 间隔时间
var_interval=StringVar()
entry_interval=Entry(frame_right,textvariable=var_interval, width=5)
entry_interval.place(relx=0.52, rely=0.02)
var_interval.set("60")
# 关键字
var_key=StringVar()
entry_key=Entry(frame_right,textvariable=var_key, width=5)
entry_key.place(relx=0.52, rely=0.22)
var_key.set("全新")
# 底部结果区
frame_bottom = LabelFrame(window, text='结   果', labelanchor="n")
frame_bottom.place(relx=0.02, rely=0.22, relwidth=0.93, relheight=0.76)
# 结果显示框
out_text=Text(frame_bottom, width=64, height=24, font=('微软雅黑',10))
out_text.place(relx=0.02, rely=0)




def show_hand_cursor(event):
    out_text.config(cursor='arrow')
def show_arrow_cursor(event):
    out_text.config(cursor='xterm')
def click(event,x):
    webbrowser.open(x)
def handlerAdaptor(fun,**kwds):
    return lambda event,fun=fun,kwds=kwds:fun(event,**kwds)

def resultlist():
    url = v_url.get()
    key = var_key.get()
    out_text.delete('1.0', END)    # 清空text
    (result_text, result_link) = gw.get_content(url, key)
    out_text.tag_config('link',foreground='blue',underline=True)
    m=0
    for each in result_text:
        out_text.tag_config(m,foreground='blue',underline=True)
        out_text.tag_bind(m,'<Enter>',show_hand_cursor)
        out_text.tag_bind(m,'<Leave>',show_arrow_cursor)

        out_text.insert(INSERT,each+'\n',m)

        out_text.tag_bind(m,'<Button-1>',handlerAdaptor(click,x=result_link[m]))
        m+=1
        # out_text.pack()

def buttonstat():

    interval = var_interval.get()
    v_time = int(interval)
    b['state'] = DISABLED
    for j in range(v_time):
        time.sleep(1)
        v_time=v_time-1
        b['text'] = str(v_time+1)
    resultlist()
    buttonstat()


def begin():
    threads = []
    #创建线程
    t1 = threading.Thread(target=buttonstat)  #  刷新按钮文字
    threads.append(t1)
    t2 = threading.Thread(target=resultlist)  #  显示结果
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

b = Button(frame_right, text=" 开 始 ", command = begin, state='normal')
b.place(relx=0.5, rely=0.55)

# 进入消息循环
window.mainloop()
#退出的函数
def usr_sign_quit():
    window.destroy()