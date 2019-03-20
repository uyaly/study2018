#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cal as calcu
from Tkinter import *
import tkMessageBox

#窗口
window = Tk()
window.title('欢迎进入学习系统')
window.geometry('500x500')
# frame = Frame(window)
# frame.pack()

# variable = StringVar()
# variable.set(OPTIONS[0])
# w = OptionMenu(window, variable, *OPTIONS)  #不加*整个列表会被作为一个选项

frame_left = LabelFrame(window, text="每种类型题目数", labelanchor="n")
frame_left.place(relx=0.02, rely=0, relwidth=0.4, relheight=0.3)


# bottomframe = Frame(window)
# bottomframe.pack( side = BOTTOM )
# leftframe = Frame(window)
# leftframe.pack( side = LEFT )


L1 = Label(frame_left,text='加法 ：... + ...')
L1.place(relx=0.02, rely=0.02)
v1=StringVar()
E1 = Entry(frame_left,textvariable=v1, width=5)
E1.place(relx=0.7, rely=0.02)
L2 = Label(frame_left,text='减法 ：... - ...')
L2.place(relx=0.02, rely=0.12)
E2 = Entry(frame_left,textvariable=v1, width=5)
E2.place(relx=0.7, rely=0.12)
L3 = Label(frame_left,text='混合1：... +/- ... +/- ...')
L3.place(relx=0.02, rely=0.22)
E3 = Entry(frame_left,textvariable=v1, width=5)
E3.place(relx=0.7, rely=0.22)
#标签
# Label(window,text='最小值:').place(x=10,y=50)
# Label(window,text='最大值:').place(x=110,y=50)
# Label(window,text='和最大值:').place(x=210,y=50)
# Label(window,text='出题数:').place(x=10,y=90)
# #最小值输入框
# var_minnum=StringVar()
# entry_minnum=Entry(window,textvariable=var_minnum, width=5)
# entry_minnum.place(x=60,y=50)
# var_minnum.set("1")
# #最大值输入框
# var_maxnum=StringVar()
# entry_maxnum=Entry(window,textvariable=var_maxnum, width=5)
# entry_maxnum.place(x=160,y=50)
# var_maxnum.set("10")
# #和最大值输入框
# var_maxsum=StringVar()
# entry_maxsum=Entry(window,textvariable=var_maxsum, width=5)
# entry_maxsum.place(x=270,y=50)
# var_maxsum.set("10")
# #出题数输入框
# var_num=StringVar()
# entry_num=Entry(window,textvariable=var_num)
# entry_num.place(x=60,y=90)
# var_num.set("100")
#标签
# var_title=StringVar()
# var_title.set("")
# title = Label(window, textvariable=var_title, width=60)
# title.place(x=10,y=140)
# #结果显示框
# out_text=Text(window, width=60, height=20)
# out_text.place(x=10,y=190)


def com():
    v_min = var_minnum.get()
    v_max = var_maxnum.get()
    v_num = var_num.get()
    v_sum = var_maxsum.get()
    v_type = variable.get()
    # 清空text
    out_text.delete('1.0', END)
    if u'加法' in v_type:
        var_title.set(u'%s以内%s %s题'% (v_sum, v_type, v_num))
        result = calcu.base_plus(int(v_min), int(v_max), int(v_sum), int(v_num))
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
    if u'减法' in v_type:
        var_title.set(u'%s以内%s %s题'% (v_sum, v_type, v_num))
        result = calcu.base_minus(int(v_min), int(v_max), int(v_sum), int(v_num))
        for i in range(len(result)):
            out_text.insert(INSERT, result[i])
    # if variable.get() == u'加减法':

        # m.add2(max,num)
        # m.minus(max,num)
        # m.minus2(max,num)

# B = Button(window, text="出 题", command = com).place(x=210,y=10)


# 进入消息循环
window.mainloop()

#退出的函数
def usr_sign_quit():
    window.destroy()