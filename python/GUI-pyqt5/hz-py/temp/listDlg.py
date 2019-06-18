import sys
from ui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class listDlg(QDialog, QMainWindow):
    def __init__(self, name="Dlg"):
        # 构造函数
        super().__init__()
        self.initUI(name)
        self.cnt_tmp = 0


    def initUI(self, name):
        # 初始化函数
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(name)
        self.initConnect()



    def initConnect(self):
        # 初始化信号与槽
        self.ui.btn_GetFile.clicked.connect(self.slot_btn_getFile)
        # pass


    def setDirEditText(self, str_show):
        # 更新edit的文本
        self.ui.edit_dir.setText( str_show )

    # ######################
    #        槽函数
    # ######################

    def slot_btn_getFile(self):
        #btn_getFile的槽函数
        self.cnt_tmp = self.cnt_tmp + 1
        self.setDirEditText(str(self.cnt_tmp))

        pass



if __name__ == '__main__':
    app = QApplication( sys.argv )
    dlg = listDlg('转换文件编码')
    dlg.show()
    sys.exit(app.exec_())
    pass
