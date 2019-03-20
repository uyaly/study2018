#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cal as calcu
from Tkinter import *
import tkMessageBox
import time
reload(sys)
sys.setdefaultencoding( "utf-8" )
#窗口
window = Tk()
window.title('欢迎进入出题系统')
window.geometry('590x650')
# 左侧题目数量
frame_left = LabelFrame(window, text="每种类型题目数", labelanchor="n")
frame_left.place(relx=0.02, rely=0, relwidth=0.4, relheight=0.4)

L1 = Label(frame_left,text='加法 ：... + ...')
L1.place(relx=0.02, rely=0.02)
v1=StringVar()
E1 = Entry(frame_left,textvariable=v1, width=5)
E1.place(relx=0.7, rely=0.02)
L2 = Label(frame_left,text='减法 ：... - ...')
L2.place(relx=0.02, rely=0.22)
v2=StringVar()
E2 = Entry(frame_left,textvariable=v2, width=5)
E2.place(relx=0.7, rely=0.22)
L3 = Label(frame_left,text='混合1：... +/- ... +/- ...')
L3.place(relx=0.02, rely=0.42)
v3=StringVar()
E3 = Entry(frame_left,textvariable=v3, width=5)
E3.place(relx=0.7, rely=0.42)
# 默认值
v1.set('50')
v2.set('50')
v3.set('8')
# L3 = Label(frame_left,text='混合1：... +/- ... +/- ...')
# L3.place(relx=0.02, rely=0.62)
# E3 = Entry(frame_left,textvariable=v1, width=5)
# E3.place(relx=0.7, rely=0.62)
# L3 = Label(frame_left,text='混合1：... +/- ... +/- ...')
# L3.place(relx=0.02, rely=0.82)
# E3 = Entry(frame_left,textvariable=v1, width=5)
# E3.place(relx=0.7, rely=0.82)

# 右侧配置区
frame_right = LabelFrame(window, text="配  置", labelanchor="n")
frame_right.place(relx=0.45, rely=0, relwidth=0.5, relheight=0.4)
#标签
Label(frame_right,text='最小值:').place(relx=0.02, rely=0.02)
Label(frame_right,text='最大值:').place(relx=0.02, rely=0.22)
#最小值输入框
var_minnum=StringVar()
entry_minnum=Entry(frame_right,textvariable=var_minnum, width=5)
entry_minnum.place(relx=0.4, rely=0.02)
var_minnum.set("1")
#最大值输入框
var_maxnum=StringVar()
entry_maxnum=Entry(frame_right,textvariable=var_maxnum, width=5)
entry_maxnum.place(relx=0.4, rely=0.22)
var_maxnum.set("20")
#标签
var_title=StringVar()
var_title.set("")
title = Label(frame_right, textvariable=var_title)
title.place(relx=0.02, rely=0.72)

# 底部结果区
frame_bottom = LabelFrame(window, text='出  题', labelanchor="n")
frame_bottom.place(relx=0.02, rely=0.4, relwidth=0.97, relheight=0.58)
#结果显示框
out_text=Text(frame_bottom, width=77, height=26)
out_text.place(relx=0.02, rely=0)


def com():
    v_min = var_minnum.get()
    v_max = var_maxnum.get()
    v_num1 = v1.get()
    v_num2 = v2.get()
    v_num3 = v3.get()
    num = 0
    # v_sum = var_maxsum.get()
    # v_type = variable.get()
    # 清空text
    out_text.delete('1.0', END)
    # 加法
    if int(v_num1)>0:
        result = calcu.base_plus(int(v_min), int(v_max), int(v_num1))
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%5 == 0:
                out_text.insert(INSERT, '\n')
        num += len(result)
    # 减法
    if int(v_num2)>0:
        result = calcu.base_minus(int(v_min), int(v_max), int(v_num2))
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%5 == 0:
                out_text.insert(INSERT, '\n')
        num += len(result)
    # 混合1
    if int(v_num3)>0:
        result = calcu.type1_str(int(v_min), int(v_max), int(v_num3))
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%4 == 0:
                out_text.insert(INSERT, '\n')
        num += len(result)

    var_title.set(u'%s以内加减法%d道'% (v_max, num))

def exportword():
    str_title = var_title+str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))) + '.doc'
    title = u'日期：'+ str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + u'   姓名：        用时：        得分：      \n'
    q = (title + out_text.get('1.0', END))
    with open(str_title, "w") as f:
        f.write(q)
    f.close()

Button(frame_right, text="出 题", command = com).place(relx=0.6, rely=0.72)
Button(frame_right, text="导 出", command = exportword).place(relx=0.8, rely=0.72)


# 进入消息循环
window.mainloop()

#退出的函数
def usr_sign_quit():
    window.destroy()