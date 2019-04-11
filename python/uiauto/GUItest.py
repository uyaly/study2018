# coding:utf-8
import subprocess
import uiautomation

var = uiautomation.RootElement()
subprocess.Popen('')    # 用进程打开程序；
window = automation.WindowControl(searchDepth = 1, ClassName = 'Notepad', RegexName = u'.* - 记事本')



window.CaptureToImage('Notepad.png') #  截图；
window.Close()    #   关闭窗口；