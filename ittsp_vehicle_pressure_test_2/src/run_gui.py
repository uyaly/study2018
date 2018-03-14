# coding:utf-8
import os,sys
import psutil
import threading
import time
from tkinter import *

CAR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CAR_PATH)
from jt808.tools import config
from src import send_thread

class Gui:
    def __init__(self):
        self.root = Tk(className='pressureTest')
        self.frame = Frame(self.root)
        self.resFrame = Frame(self.root)
        self.dateStart = StringVar()
        self.dateCount = StringVar()
        self.carCount = StringVar()
        self.gpsCount = StringVar()
        self.hearCount = StringVar()
        self.fialCount = StringVar()
        self.netCount = StringVar()
        self.cpuCount = StringVar()
        self.memoryCount = StringVar()
        self.flag = False

        self.Draw()

    def Draw(self):
        # 第一行，IP，端口
        Label(self.frame, text='IP').grid(row=0, column=0)

        self.eIP = Entry(self.frame)
        self.eIP.grid(row=0, column=1)
        self.eIP.insert(0, '192.168.3.136')

        Label(self.frame, text='Port').grid(row=0, column=2)

        self.ePort = Entry(self.frame, width=5)
        self.ePort.grid(row=0, column=3)
        self.ePort.insert(0, '5560')

        Label(self.frame, text=' ').grid(row=0, column=4)

        self.bStart = Button(self.frame, text='Start', bd=1, width=10 ,command=self.submit)
        self.bStart.grid(row=0, column=5)

        # 下面的计数器
        Label(self.resFrame, text='开始时间 : ').grid(row=0, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.dateStart).grid(row=0, column=1)
        self.dateStart.set('0000-00-00 00:00:00')

        Label(self.resFrame, text='运行时间 : ').grid(row=1, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.dateCount).grid(row=1, column=1)
        self.dateCount.set('00 day 00:00:00')

        Label(self.resFrame, text='车辆上线 : ').grid(row=2, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.carCount).grid(row=2, column=1)
        self.carCount.set('0')

        Label(self.resFrame, text='发送总GPS包 : ').grid(row=3, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.gpsCount).grid(row=3, column=1)
        self.gpsCount.set('0')

        Label(self.resFrame, text='发送总心跳包 : ').grid(row=4, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.hearCount).grid(row=4, column=1)
        self.hearCount.set('0')

        Label(self.resFrame, text='发送失败 : ').grid(row=5, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.fialCount).grid(row=5, column=1)
        self.fialCount.set('0')

        Label(self.resFrame, text='发送流量(M) : ').grid(row=6, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.netCount).grid(row=6, column=1)
        self.netCount.set('0')

        Label(self.resFrame, text='本地CPU(%) ：').grid(row=7, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.cpuCount).grid(row=7, column=1)
        self.cpuCount.set('0')

        Label(self.resFrame, text='本地内存(%) ：').grid(row=8, column=0, sticky=W)
        Label(self.resFrame, textvariable=self.memoryCount).grid(row=8, column=1)
        self.memoryCount.set('0')

        self.frame.pack(padx=10, pady=10)
        self.resFrame.pack()

        mainloop()

    def Count(self):
        config.COUNT = 0
        config.ONLINE_CAR = 0
        day, h, m, s = 0, 0, 0, 0
        self.dateStart.set(config.START_TIME)

        while self.flag:
            s += 1
            time.sleep(1)
            if(60 == s):
                m += 1
                s = 0
            elif(60 == m):
                h += 1
                m = 0
            elif(24 == h):
                day += 1
                h = 0

            self.dateCount.set('%02d day %02d:%02d:%02d' % (day, h, m, s))
            self.gpsCount.set(config.GPS)
            self.carCount.set(config.ONLINE)
            self.hearCount.set(config.HEART)
            self.fialCount.set(config.FAIL)
            self.netCount.set('%.2f' % (config.BYTES / 1024 / 1024))
            self.cpuCount.set(self.getCPUstate())
            self.memoryCount.set(self.getMemorystate())

    def submit(self):
        print(self.eIP.get(), self.ePort.get())
        ip = self.eIP.get()
        port = self.ePort.get()

        if '' == ip or '' == port:
            print('请输入ip与端口')
        # 点击开始按钮
        elif self.flag == False:
            self.flag = True
            self.bStart.config(relief=SUNKEN, text='Stop')
            thread = threading.Thread(target=self.Count)
            thread.setDaemon(True)
            thread.start()

            t = threading.Thread(target=self.threadStart, args=(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\car', ip, port))
            t.setDaemon(True)
            t.start()
        # 点击结束按钮
        else:
            self.flag = False
            self.bStart.config(relief=RAISED, text="Start")
            self.threadStop()

    def threadStart(self, fileDir, ip, port):
        print(os.getcwd())
        fileList = os.listdir(fileDir)
        filePath = os.getcwd()+'\\' + fileDir

        self.stopList = []
        for each in fileList:
            runGPS = send_thread.ThreadGPS((filePath + '\\' + each), ip, int(port))
            self.stopList.append(runGPS)
            tGPS = threading.Thread(target=runGPS.run)
            tGPS.setDaemon(True)
            tGPS.start()
            time.sleep(20)

    def threadStop(self):
        for each in self.stopList:
            each.stop()

    def getCPUstate(self):
        return (" CPU: " + str(psutil.cpu_percent()) + "%")

    #function of Get Memory
    def getMemorystate(self):
            phymem = psutil.virtual_memory()
            line = "Memory: %5s%% %6s/%s"%(
                phymem.percent,
                str(int(phymem.used/1024/1024))+"M",
                str(int(phymem.total/1024/1024))+"M"
                )
            return line


if __name__ == '__main__':
    g = Gui()
    # PATH_CAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\car'
    # print(PATH_CAR)
