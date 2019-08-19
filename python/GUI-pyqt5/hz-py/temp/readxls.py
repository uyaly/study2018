# coding:utf-8

import xlrd
class ExcelUtil:

    def dict_data(self):
        filePath = r'data.xls'
        sheetName = 'Sheet1'
        self.data = xlrd.open_workbook(filePath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        # self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        r = []
        for i in range(self.rowNum-1):
            values = self.table.row_values(i+1)
            r.append(values)
        return r

# if __name__ == "__main__":
    # filePath = r'data.xls'
    # sheetName = 'Sheet1'
    # list = ExcelUtil().dict_data(filePath, sheetName)
    # print(list)
