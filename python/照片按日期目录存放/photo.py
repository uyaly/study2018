
# -*- coding: gbk -*-
 
"""
���ܣ�����Ƭ��������ʱ����й���
ʹ�÷��������ű�����Ƭ����ͬһĿ¼��˫�����нű�����
���ߣ�����
"""
 
import shutil
import os
import time
import exifread
 
 
class ReadFailException(Exception):
    pass
 
def getOriginalDate(filename):
    try:
        fd = open(filename, 'rb')
    except:
        raise ReadFailException, "unopen file[%s]\n" % filename
    data = exifread.process_file( fd )
    if data:
        try:
            t = data['EXIF DateTimeOriginal']
            return str(t).replace(":","-")[:10]
        except:
            pass
    state = os.stat(filename)
    return time.strftime("%Y-%m-%d", time.localtime(state[-2]))
 
 
def classifyPictures(path):
    for root,dirs,files in os.walk(path,True):
        dirs[:] = []
        for filename in files:
            olddir = os.path.join(root, filename)
            f,e = os.path.splitext(olddir)
            if e.lower() not in ('.jpg','.png','.mp4','.mov','.jpeg','.heic','.gif'):
                continue
            info = "�ļ���: " + olddir + " "
            t=""
            try:
                t = getOriginalDate( olddir )
            except Exception,e:
                print e
                continue
            info = info + "����ʱ�䣺" + t + " "
            pwd = root +'\\'+ t
            newdir = pwd + '\\' + filename
            if not os.path.exists(pwd ):
                os.mkdir(pwd)
            print info, newdir
            shutil.copy2( olddir, newdir )
            os.remove( olddir )
 
if __name__ == "__main__":
    path = "..\\"
    classifyPictures(path)