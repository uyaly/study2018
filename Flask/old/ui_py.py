#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import MySQLdb
import time
import Tkinter
from Tkinter import *
from Tkconstants import *
import datetime,time
#加入以下2句可向文本中输入中文
reload(sys) 
sys.setdefaultencoding('utf8')

root = Tkinter.Tk()
root.title(u'测试工具(R9)')
root.geometry('600x450+500+300')
m = Tkinter.Message(root,text = 'Data Testing Tools',width = 200,fg = 'blue',aspect = 400)
m.pack()
m.place(x = 240,y = 5)
#m1 = Tkinter.Message(root,text = u'（整个服务器数据测试）',width = 200,fg = 'yellow',aspect = 400)
#m1.pack()
#m1.place(x = 240,y = 25)

ip = Tkinter.Label(root,text = 'IP_Address:')
ip.pack(side = LEFT,padx = 20,pady = 10)
ip.place(x = 30, y = 50)
e = Tkinter.StringVar()
add = Tkinter.Entry(root,width = 40,textvariable = e)
add.pack(side = LEFT)
e.set('192.168.1.16')
add.place(x = 120, y = 50)

v4=Tkinter.StringVar()
ch4=Tkinter.Checkbutton(root,variable = v4,text=u'只检测正在运行的数据',offvalue='0',onvalue='1')
ch4.pack(side=LEFT,padx = 20,pady = 10)
ch4.place(x = 30, y = 80)
v4.set('0')


v5=Tkinter.StringVar()
ch5=Tkinter.Checkbutton(root,variable = v5,text=u'是否选择具体的查询数据',offvalue='0',onvalue='1')
ch5.pack(side=LEFT,padx = 20,pady = 10)
ch5.place(x = 30, y = 110)
v5.set('0')



#v10=Tkinter.StringVar()
ch10=Tkinter.Checkbutton(root,variable = v5,text='',offvalue='0',onvalue='1')
ch10.pack(side=LEFT,padx = 20,pady = 10)
ch10.place(x = 70, y = 140)
#v10.set('1')
dev = Tkinter.Label(root,text = 'Dev_Type:')
dev.pack(side = LEFT,padx = 20,pady = 10)
dev.place(x = 90, y = 140)
e = Tkinter.StringVar()
de = Tkinter.Entry(root,width = 10,textvariable = e)
de.pack(side = LEFT)
e.set('22')
de.place(x = 160, y = 140)


v6=Tkinter.StringVar()
ch6=Tkinter.Checkbutton(root,variable = v6,text='',offvalue='0',onvalue='1')
ch6.pack(side=LEFT,padx = 20,pady = 10)
ch6.place(x = 280, y = 140)
v6.set('0')
zwj = Tkinter.Label(root,text = 'Dev_ID:')
zwj.pack(side = LEFT,padx = 20,pady = 10)
zwj.place(x = 310, y = 140)
e = Tkinter.StringVar()
zw = Tkinter.Entry(root,width = 5,textvariable = e)
zw.pack(side = LEFT)
e.set('1')
zw.place(x = 380, y = 140)
m6 = Tkinter.Message(root,text = u'到',width = 200,fg = 'blue',aspect = 400)
m6.pack()
m6.place(x = 420,y = 140)
e = Tkinter.StringVar()
devn = Tkinter.Entry(root,width = 5,textvariable = e)
devn.pack(side = LEFT)
e.set('1')
devn.place(x = 450, y = 140)

v7=Tkinter.StringVar()
ch7=Tkinter.Checkbutton(root,variable = v7,text='',offvalue='0',onvalue='1')
ch7.pack(side=LEFT,padx = 20,pady = 10)
ch7.place(x = 280, y = 170)
v7.set('0')
unit = Tkinter.Label(root,text = 'Unit_ID:')
unit.pack(side = LEFT,padx = 20,pady = 10)
unit.place(x = 310, y = 170)
e = Tkinter.StringVar()
un = Tkinter.Entry(root,width = 5,textvariable = e)
un.pack(side = LEFT)
e.set('1')
un.place(x = 380, y = 170)
m7 = Tkinter.Message(root,text = u'到',width = 200,fg = 'blue',aspect = 400)
m7.pack()
m7.place(x = 420,y = 170)
e = Tkinter.StringVar()
ucu = Tkinter.Entry(root,width = 5,textvariable = e)
ucu.pack(side = LEFT)
e.set('1')
ucu.place(x = 450, y = 170)


v8=Tkinter.StringVar()
ch8=Tkinter.Checkbutton(root,variable = v8,text='',offvalue='0',onvalue='1')
ch8.pack(side=LEFT,padx = 20,pady = 10)
ch8.place(x = 280, y = 200)
v8.set('0')
chl = Tkinter.Label(root,text = 'Chl_ID:')
chl.pack(side = LEFT,padx = 20,pady = 10)
chl.place(x = 310, y = 200)
e = Tkinter.StringVar()
co = Tkinter.Entry(root,width = 5,textvariable = e)
co.pack(side = LEFT)
e.set('1')
co.place(x = 380, y = 200)
m8 = Tkinter.Message(root,text = u'到',width = 200,fg = 'blue',aspect = 400)
m8.pack()
m8.place(x = 420,y = 200)
e = Tkinter.StringVar()
ccu = Tkinter.Entry(root,width = 5,textvariable = e)
ccu.pack(side = LEFT)
e.set('1')
ccu.place(x = 450, y = 200)



v9=Tkinter.StringVar()
ch9=Tkinter.Checkbutton(root,variable = v9,text='',offvalue='0',onvalue='1')
ch9.pack(side=LEFT,padx = 20,pady = 10)
ch9.place(x = 280, y = 230)
v9.set('0')
test = Tkinter.Label(root,text = 'test_id:')
test.pack(side = LEFT,padx = 20,pady = 10)
test.place(x = 310, y = 230)
e = Tkinter.StringVar()
te = Tkinter.Entry(root,width = 5,textvariable = e)
te.pack(side = LEFT)
e.set('1')
te.place(x = 380, y = 230)
m9 = Tkinter.Message(root,text = u'到',width = 200,fg = 'blue',aspect = 400)
m9.pack()
m9.place(x = 420,y = 230)
e = Tkinter.StringVar()
tcu = Tkinter.Entry(root,width = 5,textvariable = e)
tcu.pack(side = LEFT)
e.set('1')
tcu.place(x = 450, y = 230)








#m2 = Tkinter.Message(root,text = u'（到）',width = 200,fg = 'yellow',aspect = 400)
#m2.pack()
#m2.place(x = 150,y = 190)


########
v=Tkinter.StringVar()
ch=Tkinter.Checkbutton(root,variable = v,text=u'辅助通道',offvalue='0',onvalue='1')
ch.pack(side=LEFT,padx = 20,pady = 10)
ch.place(x = 30, y = 260)
v.set('0')

v1=Tkinter.StringVar()
ch1=Tkinter.Checkbutton(root,variable = v1,text=u'记录序号',offvalue='0',onvalue='1')
ch1.pack(side=LEFT,padx = 20,pady = 10)
ch1.place(x = 120, y = 260)
v1.set('0')

v2=Tkinter.StringVar()
ch2=Tkinter.Checkbutton(root,variable = v2,text=u'记录时间',offvalue='0',onvalue='1')
ch2.pack(side=LEFT,padx = 20,pady = 10)
ch2.place(x = 120, y = 290)
v2.set('0')

v3=Tkinter.StringVar()
ch3=Tkinter.Checkbutton(root,variable = v3,text=u'绝对时间',offvalue='0',onvalue='1')
ch3.pack(side=LEFT,padx = 20,pady = 10)
ch3.place(x = 120, y = 320)
v3.set('0')

def main():
    ip_address = add.get()
    aux = int(v.get())
    xz1=int(v1.get())
    xz2=int(v2.get())
    xz3=int(v3.get())
    
    conn = MySQLdb.connect(host = ip_address,user="BtsServer",passwd="www.neware.com.cn",db="bts63",port=3306)
    cur = conn.cursor()
    cur1= conn.cursor()
    cur2= conn.cursor()
    
    load=os.getcwd()+"\\log.txt"
    logload=open(load,'a')
    log=str(ip_address)+'\n'
    logload.write(log)
    
    #print aux
    #sql='select * from h_test order by dev_uid asc,unit_id ASC,chl_id ASC,test_id ASC'  #asc 表示升序 , desc表示降序
    sql=cs_sql()
    print '------------------>\n'
    print u'查询数据'
    print '------------------>\n'
    print sql
    cur1.execute(sql)
    htestrows=int(cur1.rowcount)
    for ii in range(htestrows):
        row=cur1.fetchone()
        dev_uid=row[1]
        unit_id=row[2]
        chl_id=row[3]
        test_id=row[0]
        main_first_table=row[17]
        main_second_table=row[18]
        aux_first_table=row[19]
        aux_second_table=row[20]
        if dev_uid==None or dev_uid=='':
            print ii
            break
        if  xz1==0 and xz2==0 and xz3==0:
            print 'cuowu'
            break
        log =str(dev_uid)+'_'+str(unit_id)+'_'+str(chl_id)+'_'+str(test_id)+'\n'
        print log
        logload.write(log)
        L1=-500000
        L2=0
        aux_e=aux_f='2012-11-08 11:43:25'
        sql='SELECT * FROM '+str(main_first_table)+' WHERE unit_id='+str(unit_id)+' AND chl_id='+str(chl_id)+' AND test_id='+str(test_id)+' and seq_id=2'
        cur.execute(sql)
        aa=int(cur.rowcount)
        if aa==1:
            row=cur.fetchone()
            record_time=row[9]
        elif aa>1:
            print u'未知错误'
        else:
            print dev_uid,'_',unit_id,'_',chl_id,'_',test_id,u'数据条数为：0'
        if aux==1:
            aux_sql='SELECT * FROM h_bts612_chlmap WHERE dev_uid=' + str(dev_uid)+' and unit_id='+str(unit_id)+' AND chl_map_id='+str(chl_id)+' AND test_id='+str(test_id) #+ ' AND seq_id=1'
            cur.execute(aux_sql)
            auxs=int(cur.rowcount)-1
            print u'辅助通道个数为: ',auxs
            log = u'辅助通道个数为: '+str(auxs)+'\n'
            logload.write(log)
        aux_cyc=cyc=0
        aux_st_id=st_id=0
        aux_xu1=xu1=0
        aux_xu2=xu2=0
        aux_xu3=xu3=0
        aux_re_t1=re_t1=0
        aux_re_t2=re_t2=0
        aux_re_t3=re_t3=0
        aux_ju_t1=ju_t1='2012-11-08 11:43:25'
        aux_ju_t2=ju_t2='2012-11-08 11:43:25'
        aux_ju_t3=ju_t3='2012-11-08 11:43:25'
        for d in range(100):
            L1=L1+500000
            L2=L2+500000
            if d == 0:
                #global sql
                sql='SELECT * FROM '+str(main_first_table)+' WHERE unit_id='+str(unit_id)+' AND chl_id='+str(chl_id)+' AND test_id='+str(test_id)
            elif d > 0:
                sql='SELECT * FROM '+str(main_second_table)+' WHERE unit_id='+str(unit_id)+' AND chl_id='+str(chl_id)+' AND test_id='+str(test_id)+' AND seq_id>'+str(L1)+' AND seq_id<='+str(L2)
                if main_second_table==None or main_second_table=='':
                    break
            else:
                print u'未知错误'
                log=u'未知错误'+'\n'
                logload.write(log)
                break
            cur2.execute(sql)
            numrows=int(cur2.rowcount)
            if d>0 and numrows==0:
                break
            elif d+numrows==0 :
                print u"通道数据为：0"
            else: 
                print '<-----',d,'----->'
                print sql
                print u'主通道数据条数',numrows
                for i in range(numrows):
                    row=cur2.fetchone()
                    xu1=xu2
                    xu2=xu3
                    xu3=row[3]
                    re_t1=re_t2
                    re_t2=re_t3
                    re_t3=row[9]
                    ju_t1=ju_t2
                    ju_t2=ju_t3
                    ju_t3=row[23]
                    ju_t3=str(ju_t3)
                    if i%1000==0:
                        print u'主通道：Please wait...' 
                    if xz1==1 and xu3-xu2>1:
                        print u'主通道缺少的数据有：','\n',xu2,'~',xu3
                        log=u'主通道缺少的数据有：'+'\n'+str(xu2)+'~'+str(xu3)+'\n'
                        logload.write(log)
                    elif xz1==1 and xu3-xu2<1:
                        print u'主通道记录号变小','\n',xu2,'   ',re_t2,'\n',xu3,'   ',re_t3
                        log=u'主通道记录号变小'+'\n'+str(xu2)+'  '+str(re_t2)+'\n'+str(xu3)+'  '+str(re_t3)+'\n'
                        logload.write(log)
                    #elif xz1==0:
                        #print u'weicesi ID'
                    if xz2==1:
                        if cyc==row[4] and st_id==row[5] and  (re_t2-re_t1)==(re_t3-re_t2):
                            record_time=re_t3-re_t2
                            r_t=row[9]
                        elif cyc==row[4] and st_id==row[5] and re_t2-re_t1>record_time and re_t3-re_t2==record_time:
                            print u'记录时间不连续的数据'
                            log=u'记录时间不连续的数据'+'\n'
                            logload.write(log)
                            print u'记录序号',u'记录时间'
                            log=u'记录序号  记录时间'+'\n'
                            logload.write(log)
                            print xu1,'   ',re_t1
                            log=str(xu1)+'      '+str(re_t1)+'\n'
                            logload.write(log)
                            print xu2,'   ',re_t2
                            log=str(xu2)+'      '+str(re_t2)+'\n'
                            logload.write(log)
                            r_t=row[9]
                        else:
                            r_t=row[9]
                    #else:
                        #print 'weics record time'
                    if xz3==1 and ju_t3<ju_t2:
                        log=u'主通道绝对时间有问题的数据'+'\n'
                        print log
                        print xu2,'      ',ju_t2
                        print xu3,'      ',ju_t3
                        logload.write(log)
                        log=str(xu2)+'      '+str(ju_t2)+'\n'
                        logload.write(log)
                        log=str(xu3)+'      '+str(ju_t3)+'\n'
                    #elif xz3==0:
                        #print 'weics realtime'


                    cyc=row[4]
                    st_id=row[5]
                    
                    
            if aux==1 and auxs>0:
                c1=aux_xu1
                c2=aux_xu2
                c3=aux_xu3
                c4=aux_re_t1
                c5=aux_re_t2
                c6=aux_re_t3
                c7=aux_ju_t1
                c8=aux_ju_t2
                c9=aux_ju_t3
                c10=aux_cyc
                c11=aux_st_id
                for p in range(auxs):
                    aux_xu1=c1
                    aux_xu2=c2
                    aux_xu3=c3
                    aux_re_t1=c4
                    aux_re_t2=c5
                    aux_re_t3=c6
                    aux_ju_t1=c7
                    aux_ju_t2=c8
                    aux_ju_t3=c9
                    aux_cyc=c10
                    aux_st_id=c11
                    if d==0:
                        aux_sql='SELECT * FROM '+str(aux_first_table)+' WHERE unit_id='+str(unit_id)+' AND chl_id='+str(chl_id)+' AND test_id='+str(test_id)+' AND auxchl_id='+str(p+1)
                    else :
                        aux_sql='SELECT * FROM '+str(aux_second_table)+' WHERE unit_id='+str(unit_id)+' AND chl_id='+str(chl_id)+' AND test_id='+str(test_id)+' AND auxchl_id='+str(p+1)+' AND seq_id>'+str(L1)+' AND seq_id<='+str(L2)
                        if aux_second_table==None:
                            break
                    cur2.execute(aux_sql)
                    aux_numrows=int(cur2.rowcount)
                    print d
                    print aux_sql
                    print u'辅助通道',str(p),u'数据条数',aux_numrows

                    for i in range(aux_numrows):
                        row=cur2.fetchone()
                        aux_xu1=aux_xu2
                        aux_xu2=aux_xu3
                        aux_xu3=row[5]
                        aux_re_t1=aux_re_t2
                        aux_re_t2=aux_re_t3
                        aux_re_t3=row[11]
                        aux_ju_t1=aux_ju_t2
                        aux_ju_t2=aux_ju_t3
                        aux_ju_t3=row[25]
                        aux_ju_t3=str(aux_ju_t3)
                        if i%1000==0:
                            print u'辅助通道：Please wait...' 
                        if xz1==1 and aux_xu3-aux_xu2>1:
                            print u'辅助通道缺少的数据有：','\n',aux_xu2,'~',aux_xu3
                            log=u'辅助通道缺少的数据有：'+'\n'+str(aux_xu2)+'~'+str(aux_xu3)+'\n'
                            logload.write(log)
                        elif xz1==1 and aux_xu3-aux_xu2<1:
                            print u'辅助通道记录号变小','\n',aux_xu2,'   ',aux_re_t2,'\n',aux_xu3,'   ',aux_re_t3
                            log=u'辅助通道记录号变小'+'\n'+str(aux_xu2)+'  '+str(aux_re_t2)+'\n'+str(aux_xu3)+'  '+str(aux_re_t3)+'\n'
                            logload.write(log)
                    #elif xz1==0:
                        #print u'weicesi ID'
                        if xz2==1:
                            if aux_cyc==row[6] and aux_st_id==row[7] and  (aux_re_t2-aux_re_t1)==(aux_re_t3-aux_re_t2):
                                record_time=aux_re_t3-aux_re_t2
                                aux_r_t=row[11]
                            elif aux_cyc==row[6] and aux_st_id==row[7] and aux_re_t2-aux_re_t1>record_time and aux_re_t3-aux_re_t2==record_time:
                                print u'辅助通道记录时间不连续的数据'
                                log=u'辅助通道记录时间不连续的数据'+'\n'
                                logload.write(log)
                                print u'记录序号',u'记录时间'
                                log=u'记录序号  记录时间'+'\n'
                                logload.write(log)
                                print aux_xu1,'   ',aux_re_t1
                                log=str(aux_xu1)+'      '+str(aux_re_t1)+'\n'
                                logload.write(log)
                                print aux_xu2,'   ',aux_re_t2
                                log=str(aux_xu2)+'      '+str(aux_re_t2)+'\n'
                                logload.write(log)
                                aux_r_t=row[11]
                            else:
                                aux_r_t=row[11]
                    #else:
                        #print 'weics record time'
                        if xz3==1 and aux_ju_t3<aux_ju_t2:
                            log=u'辅助通道绝对时间有问题的数据'+'\n'
                            print log
                            print aux_xu2,'      ',aux_ju_t2
                            print aux_xu3,'      ',aux_ju_t3
                            logload.write(log)
                            log=str(aux_xu2)+'      '+str(aux_ju_t2)+'\n'
                            logload.write(log)
                            log=str(aux_xu3)+'      '+str(aux_ju_t3)+'\n'
                    #elif xz3==0:
                        #print 'weics realtime'
                        aux_cyc=row[6]
                        aux_st_id=row[7]

        log='\n'
        logload.write(log)
        print u'测试ID:',test_id,u'测试完成'
            
    print('finish!')
    #logload.close()
    conn.commit()
    cur1.close()
    cur.close()
    conn.close()



#删除日志
def maine():
    os.getcwd()
    try:
        os.remove( 'log.txt' )
    except  WindowsError:
        pass
    


def cs_sql():
    a1=int(v4.get())
    a2=int(v5.get())
    #a3=int(v10.get())
    a4=int(v6.get())
    a5=int(v7.get())
    a6=int(v8.get())
    a7=int(v9.get())
    dev_type = int(de.get())
    dev_id = int(zw.get())
    dev_uid = dev_type * 10000 + dev_id

    first_unit_id = int(un.get())
    first_chl_id = int(co.get())
    first_test_id = int(te.get())
    
    dev_count=int(devn.get())
    unit_count =int(ucu.get())
    chl_count =int(ccu.get())
    test_count =int(tcu.get())

    
    s=' order by dev_uid asc,unit_id ASC,chl_id ASC,test_id ASC'
    if a1==1:
        sql='select * from test'
        sq=sql+s
    else:
        sql='select * from h_test'
        sq=sql+s
    #print sq
    if a2==1:
        if a4==1:
            if dev_count==None or dev_count==1:
                b=' where dev_uid='+str(dev_uid)
            else:
                b=' where dev_uid>='+str(dev_uid)+' and dev_uid<='+str(dev_type*10000+dev_count)
        else:
            b=' where dev_uid>='+str(dev_type*10000)+' and dev_uid<=' +str(dev_type*10000+256)
        if a5==1:
            if unit_count==None or unit_count==1:
                b2=' and unit_id='+str(first_unit_id)
            else:
                b2=' and unit_id>='+str(first_unit_id)+' and unit_id<='+str(unit_count)
        else:
            b2=''
        if a6==1:
            if chl_count==None or chl_count==1:
                b3=' and chl_id='+str(first_chl_id)
            else:
                b3=' and chl_id>='+str(first_chl_id)+' and chl_id<='+str(chl_count)
        else:
            b3=''
        if a7==1:
            if test_count==None or test_count==1:
                b4=' and test_id='+str(first_test_id)
            else:
                b4=' and test_id>='+str(first_test_id)+' and test_id<='+str(test_count)
        else:
            b4=''
        sq=sql+b+b2+b3+b4+s
    return sq
        



#main
button = Tkinter.Button(root,text = u"全部",fg = 'blue',bg = 'gray',width = 8,height = 1,command = main)
button.pack(side = RIGHT)
button.place(x = 60,y = 360)


button = Tkinter.Button(root,text = u"退出",fg = 'blue',bg = 'gray',width = 8,height = 1,command = root.destroy)
button.pack(side = RIGHT)
button.place(x = 460,y = 400)

button = Tkinter.Button(root,text = u"删除日志",fg = 'blue',bg = 'gray',width = 8,height = 1,command =maine)
button.pack(side = RIGHT)
button.place(x = 460,y = 360)






root.mainloop()
