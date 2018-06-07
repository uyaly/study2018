import xlrd
cls = []
def getXLS(sheetName):
    """
    get the value in excel
    :param sheetName
    :return:cls
    """

    if len(cls) == 0:
        xlsPath = os.path.join(readConfig.prjDir, "testSet\\bsns", "TestCase.xls")

        #read the excel
        data = xlrd.open_workbook(xlsPath)

        #get the sheet
        table = data.sheet_by_name(sheetName)

        nrows = table.nrows

        for i in range(nrows):

            if table.row_values(i)[0] != 'userName':
                cls.append(table.row_values(i))
    return cls