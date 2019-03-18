#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math as m
import Tkinter as tk
import tkMessageBox

#窗口
window = tk.Tk()
window.title('欢迎进入学习系统')
window.geometry('450x300')

OPTIONS = [
    '加法',
    '减法',
    '加减法',
    '。。。'
    ]
variable = tk.StringVar()
variable.set(OPTIONS[0])
w = tk.OptionMenu(window, variable, *OPTIONS)  #不加*整个列表会被作为一个选项
w.place(x=10,y=10)
#标签
tk.Label(window,text='最小值:').place(x=10,y=50)
tk.Label(window,text='最大值:').place(x=110,y=50)
tk.Label(window,text='出题数:').place(x=10,y=90)
#最小值输入框
var_minnum=tk.StringVar()
entry_minnum=tk.Entry(window,textvariable=var_minnum, width=5)
entry_minnum.place(x=60,y=50)
#最大值输入框
var_maxnum=tk.StringVar()
entry_maxnum=tk.Entry(window,textvariable=var_maxnum, width=5)
entry_maxnum.place(x=160,y=50)
#出题数输入框
var_num=tk.StringVar()
entry_num=tk.Entry(window,textvariable=var_num)
entry_num.place(x=60,y=90)
#结果显示框
var_text=tk.StringVar()
out_text=tk.Text(window,textvariable=var_text, width=50)
out_text.place(x=10,y=130)

result=m.add(var_maxnum,var_num)
# m.add2(var_maxnum,var_num)
# m.minus(var_maxnum,var_num)
# m.minus2(var_maxnum,var_num)


B = tk.Button(window, text ="出 题", command = '').place(x=250,y=90)


# 进入消息循环
window.mainloop()

#退出的函数
def usr_sign_quit():
    window.destroy()