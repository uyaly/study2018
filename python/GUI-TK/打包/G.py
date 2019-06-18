#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cal_2 as calcu
from Tkinter import *
import tkMessageBox
import random
import time
reload(sys)
sys.setdefaultencoding( "utf-8" )
#窗口
window = Tk()
window.title('欢迎进入出题系统')
window.geometry('560x460')

# OPTIONS = [
#     # '加法 ：... + ... ',
#     # '减法 ：... - ... ',
#     # '混合1：... +/- ... +/- ...',
#     # '混合2：... +/- ... x ...',
#     # '混合3：(... +/- ...) / ...',
#     ]
# variable = StringVar()
# variable.set(OPTIONS[2])
# w = OptionMenu(window, variable, *OPTIONS)  #不加*整个列表会被作为一个选项
# w.place(x=10,y=10)

#标签
Label(window,text='最小值:').place(x=10,y=10)
Label(window,text='最大值:').place(x=110,y=10)
# Label(window,text='和最大值:').place(x=210,y=50)
Label(window,text='出题数:').place(x=210,y=10)

#最小值输入框
var_minnum=StringVar()
entry_minnum=Entry(window,textvariable=var_minnum, width=5)
entry_minnum.place(x=60,y=10)
var_minnum.set("1")
#最大值输入框
var_maxnum=StringVar()
entry_maxnum=Entry(window,textvariable=var_maxnum, width=5)
entry_maxnum.place(x=160,y=10)
var_maxnum.set("10")
#出题数输入框
var_num=StringVar()
entry_num=Entry(window,textvariable=var_num, width=5)
entry_num.place(x=270,y=10)
var_num.set("160")
#标签,标题
var_title=StringVar()
var_title.set("")
title = Label(window, textvariable=var_title, width=50)
title.place(x=300,y=5)
#标签，重复统计
var_same=StringVar()
var_same.set("")
same = Label(window, textvariable=var_same, width=50)
same.place(x=300,y=25)
#结果显示框
out_text=Text(window, width=77, height=30)
out_text.place(x=10,y=60)

def com():
    v_min = var_minnum.get()
    v_max = var_maxnum.get()
    v_num = var_num.get()
    # 清空text
    out_text.delete('1.0', END)
    num_plus = int(v_num)//2
    result_plus = calcu.base_plus(int(v_min), int(v_max), num_plus)
    result_minus = (calcu.base_minus(int(v_min), int(v_max), int(v_num)- num_plus))
    result = result_plus + result_minus
    random.shuffle(result)
    for i in range(int(v_num)):
        out_text.insert(INSERT, result[i])
        if (i+1)%5 == 0:
            out_text.insert(INSERT, '\n')
    var_title.set(u'%s以内口算%s题'% (v_max, v_num))
    # 统计数组中的重复项
    # for j in set(result):
        # print('{0}个数：{1}'.format(j, result.count(j)))
    var_same.set('重复个数为：{0}'.format(int(v_num)-len(set(result))))


def exportword():
    str_title = var_title.get()+ str(time.strftime('%Y%m%d',time.localtime(time.time()))) + '.doc'
    # str_title = var_title.get()+ str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))) + '.doc'
    title = u'日期：'+ str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + u'   姓名：        用时：        得分：      \n'
    q = (title + out_text.get('1.0', END))
    with open(str_title, "w") as f:
        f.write(q)
    f.close()
    # tkMessageBox.showinfo("提示", "已导出", parent=window)

Button(window, text="出 题", command = com).place(x=330,y=5)
Button(window, text="导 出", command = exportword).place(x=380,y=5)

# 进入消息循环
window.mainloop()

#退出的函数
def usr_sign_quit():
    window.destroy()