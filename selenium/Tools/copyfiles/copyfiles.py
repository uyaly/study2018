# coding:utf-8
import os
import shutil
import xlrd
class copyfiles():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # # 获取第一行作为key值
        # self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                # for x in range(self.colNum):
                    # s[self.keys[x]] = values[x]
                # r.append(s)
                r.append(values)
                j+=1
            return r
    def shutil(self, newPath):
        # alllist=os.listdir(u"D:\\notes\\python\\资料\\")
        data = copyfiles(filePath, sheetName)
        oldpath = data.dict_data()

        for i in range(len(oldpath)):
            print oldpath
            print oldpath[i].split(".")
            # aa,bb=oldpath.split(".")
            # aa,bb=i.split(".")
            # if 'python' in aa.lower():
                # oldname= u"E:\\notes\\python\\资料\\"+aa+"."+bb
            # newname=u"E:\\files\\"+ aa+"." + bb
            # shutil.copyfile(oldpath,newname)
if __name__ == "__main__":
    # 注意：此代码if以上的勿乱改，调用此方法只需修改两个参数，一个是excelPath存放xlsx的路径，另外一个是sheetName的值
    filePath = r"E:\PycharmProjects\test\study\selenium\Tools\copyfiles\data.xlsx"
    sheetName = "Sheet1"
    newPath = r"E:\4"
    data = copyfiles(filePath, sheetName)
    data.shutil(newPath)