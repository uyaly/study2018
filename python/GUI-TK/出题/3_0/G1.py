#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cal_3 as calcu
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
frame_left.place(relx=0.02, rely=0, relwidth=0.4, relheight=0.3)

Label(frame_left,text='加法 ：... + ...').place(relx=0.02, rely=0.02)
v1=StringVar()
Entry(frame_left,textvariable=v1, width=5).place(relx=0.7, rely=0.02)

Label(frame_left,text='减法 ：... - ...').place(relx=0.02, rely=0.15)
v2=StringVar()
Entry(frame_left,textvariable=v2, width=5).place(relx=0.7, rely=0.15)

L3 = Label(frame_left,text='乘法 ：... * ...').place(relx=0.02, rely=0.28)
v3=StringVar()
E3 = Entry(frame_left,textvariable=v3, width=5).place(relx=0.7, rely=0.28)

L4 = Label(frame_left,text='除法 ：... / ...').place(relx=0.02, rely=0.41)
v4=StringVar()
E4 = Entry(frame_left,textvariable=v4, width=5).place(relx=0.7, rely=0.41)

L5 = Label(frame_left,text='混合1：... +/- ... +/- ...').place(relx=0.02, rely=0.54)
v5=StringVar()
E5 = Entry(frame_left,textvariable=v5, width=5).place(relx=0.7, rely=0.54)

L6 = Label(frame_left,text='混合2：... +/- ... x ...').place(relx=0.02, rely=0.67)
v6=StringVar()
E6 = Entry(frame_left,textvariable=v6, width=5).place(relx=0.7, rely=0.67)

L7 = Label(frame_left,text='混合3：(... +/- ...) / ...').place(relx=0.02, rely=0.80)
v7=StringVar()
E7 = Entry(frame_left,textvariable=v7, width=5).place(relx=0.7, rely=0.80)
# 默认值
v1.set('100')
# v2.set('5')
# v3.set('5')
# v4.set('5')
# v5.set('4')
# v6.set('4')
# v7.set('4')

# 右侧配置区
frame_right = LabelFrame(window, text="配  置", labelanchor="n")
frame_right.place(relx=0.45, rely=0, relwidth=0.5, relheight=0.3)
#标签
Label(frame_right,text='最小值:').place(relx=0.02, rely=0.02)
Label(frame_right,text='最大值:').place(relx=0.02, rely=0.22)
Label(frame_right,text='和最小值:').place(relx=0.02, rely=0.42)
Label(frame_right,text='和最大值:').place(relx=0.02, rely=0.62)
#最小值输入框
var_minnum=StringVar()
entry_minnum=Entry(frame_right,textvariable=var_minnum, width=5)
entry_minnum.place(relx=0.4, rely=0.02)
var_minnum.set("1")
#最大值输入框
var_maxnum=StringVar()
entry_maxnum=Entry(frame_right,textvariable=var_maxnum, width=5)
entry_maxnum.place(relx=0.4, rely=0.22)
var_maxnum.set("9")
#和最小值输入框
var_minsum=StringVar()
entry_minnum=Entry(frame_right,textvariable=var_minsum, width=5)
entry_minnum.place(relx=0.4, rely=0.42)
var_minsum.set("1")
#和最大值输入框
var_maxsum=StringVar()
entry_maxnum=Entry(frame_right,textvariable=var_maxsum, width=5)
entry_maxnum.place(relx=0.4, rely=0.62)
var_maxsum.set("100")

#标签
var_title=StringVar()
var_title.set("")
title = Label(frame_right, textvariable=var_title)
title.place(relx=0.02, rely=0.85)

# 底部结果区
frame_bottom = LabelFrame(window, text='出  题', labelanchor="n")
frame_bottom.place(relx=0.02, rely=0.3, relwidth=0.97, relheight=0.58)
#结果显示框
out_text=Text(frame_bottom, width=77, height=26)
out_text.place(relx=0.02, rely=0)


def com():
    num = []
    v_min = var_minnum.get()
    v_max = var_maxnum.get()
    v_summin  = var_minsum.get()
    v_summax  = var_maxsum.get()
    v_num = [v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get()]
    # 对输入空的改为0，即不出这种题
    for j in range(0, 7):
        try:
            num.append(int(v_num[j]))
        except:
            num.append(0)
            pass

    count = 0
    # 清空text
    out_text.delete('1.0', END)
    # 加法
    if num[0]>0:
        result = calcu.base_plus(int(v_min), int(v_max), num[0])
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%5 == 0:
                out_text.insert(INSERT, '\n')
        count += len(result)
    # 减法
    if num[1]>0:
        result = calcu.base_minus(int(v_min), int(v_max), num[1])
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%5 == 0:
                out_text.insert(INSERT, '\n')
        count += len(result)
    # 乘法
    if num[2]>0:
        result = calcu.base_multi(int(v_min), int(v_max), num[2])
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%5 == 0:
                out_text.insert(INSERT, '\n')
        count += len(result)
    # 除法
    if num[3]>0:
        result = calcu.base_div(int(v_min), int(v_max), num[3])
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%5 == 0:
                out_text.insert(INSERT, '\n')
        count += len(result)
    # 混合1
    if num[4]>0:
        result = calcu.type1_str(int(v_summin), int(v_summax), num[4])
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%4 == 0:
                out_text.insert(INSERT, '\n')
        count += len(result)
    # 混合2
    if num[5]>0:
        result = calcu.type2_str(int(v_min), int(v_max), int(v_summin), int(v_summax), num[5])
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%4 == 0:
                out_text.insert(INSERT, '\n')
        count += len(result)
    # 混合3
    if num[6]>0:
        result = calcu.type3_str(int(v_min), int(v_max), int(v_summin), int(v_summax), num[6])
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
            if (i+1)%4 == 0:
                out_text.insert(INSERT, '\n')
        count += len(result)

    var_title.set(u'%s以内加减法%s道'% (v_max, str(count)))

def exportword():
    str_title = var_title.get() + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + '.doc'
    title = u'日期：'+ str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + u'   姓名：        用时：        得分：      \n'
    q = (title + out_text.get('1.0', END))
    with open(str_title, "w") as f:
        f.write(q)
    f.close()

Button(frame_right, text=" 出 题 ", command = com).place(relx=0.6, rely=0.80)
Button(frame_right, text=" 导 出 ", command = exportword).place(relx=0.8, rely=0.80)


# 进入消息循环
window.mainloop()

#退出的函数
def usr_sign_quit():
    window.destroy()