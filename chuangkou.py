# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import tongji
import window


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Form(QMainWindow):
    absolute_path = ''

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = window.Ui_mainWindow()

        self.ui.setupUi(self)

        # self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        # 信号连接
        self.ui.toolButton.clicked.connect(self.toolButton_click)

     # 文件导入
    def toolButton_click(self):
        # absolute_path is a QString object
        absolute_path = QFileDialog.getOpenFileName(
            self, "open C file", ".", "Txt files(*.c);;Txt files(*.cpp)")
        print(absolute_path)
        if absolute_path[0]:
            self.ui.lineEdit.setText(absolute_path[0])
            self.ui.lineEdit.setReadOnly(True)
            num = tongji.Count(absolute_path[0])
            self.ui.label_zfn.setText(str(num.charCount))
            self.ui.label_csn.setText(str(num.wordCount))
            self.ui.label_hsn.setText(str(num.lineCount))
            self.ui.label_dmhn.setText(str(num.codeLines))
            self.ui.label_khn.setText(str(num.emptyLines))
            self.ui.label_zshn.setText(str(num.commentLines))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Form()  # MyForm是自己的窗体类名
    myapp.show()
    sys.exit(app.exec_())
