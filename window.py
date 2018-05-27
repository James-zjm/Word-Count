# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\10605\Desktop\statistics\window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(416, 337)
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(52, 50, 271, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(320, 49, 40, 22))
        self.toolButton.setObjectName("toolButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(52, 90, 307, 201))
        self.groupBox.setObjectName("groupBox")
        self.label_zf = QtWidgets.QLabel(self.groupBox)
        self.label_zf.setGeometry(QtCore.QRect(20, 41, 54, 12))
        self.label_zf.setObjectName("label_zf")
        self.label_zfn = QtWidgets.QLabel(self.groupBox)
        self.label_zfn.setGeometry(QtCore.QRect(80, 41, 54, 12))
        self.label_zfn.setText("")
        self.label_zfn.setObjectName("label_zfn")
        self.label_cs = QtWidgets.QLabel(self.groupBox)
        self.label_cs.setGeometry(QtCore.QRect(20, 94, 54, 12))
        self.label_cs.setObjectName("label_cs")
        self.label_hs = QtWidgets.QLabel(self.groupBox)
        self.label_hs.setGeometry(QtCore.QRect(20, 147, 54, 12))
        self.label_hs.setObjectName("label_hs")
        self.label_dmh = QtWidgets.QLabel(self.groupBox)
        self.label_dmh.setGeometry(QtCore.QRect(160, 41, 54, 12))
        self.label_dmh.setObjectName("label_dmh")
        self.label_kh = QtWidgets.QLabel(self.groupBox)
        self.label_kh.setGeometry(QtCore.QRect(160, 94, 54, 12))
        self.label_kh.setObjectName("label_kh")
        self.label_zsh = QtWidgets.QLabel(self.groupBox)
        self.label_zsh.setGeometry(QtCore.QRect(160, 147, 54, 12))
        self.label_zsh.setObjectName("label_zsh")
        self.label_csn = QtWidgets.QLabel(self.groupBox)
        self.label_csn.setGeometry(QtCore.QRect(80, 94, 54, 12))
        self.label_csn.setText("")
        self.label_csn.setObjectName("label_csn")
        self.label_hsn = QtWidgets.QLabel(self.groupBox)
        self.label_hsn.setGeometry(QtCore.QRect(80, 147, 54, 12))
        self.label_hsn.setText("")
        self.label_hsn.setObjectName("label_hsn")
        self.label_dmhn = QtWidgets.QLabel(self.groupBox)
        self.label_dmhn.setGeometry(QtCore.QRect(220, 40, 54, 12))
        self.label_dmhn.setText("")
        self.label_dmhn.setObjectName("label_dmhn")
        self.label_khn = QtWidgets.QLabel(self.groupBox)
        self.label_khn.setGeometry(QtCore.QRect(220, 94, 54, 12))
        self.label_khn.setText("")
        self.label_khn.setObjectName("label_khn")
        self.label_zshn = QtWidgets.QLabel(self.groupBox)
        self.label_zshn.setGeometry(QtCore.QRect(220, 147, 54, 12))
        self.label_zshn.setText("")
        self.label_zshn.setObjectName("label_zshn")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.toolButton.setText(_translate("mainWindow", "..."))
        self.groupBox.setTitle(_translate("mainWindow", "统计信息"))
        self.label_zf.setText(_translate("mainWindow", "字符数："))
        self.label_cs.setText(_translate("mainWindow", "词 数："))
        self.label_hs.setText(_translate("mainWindow", "行 数："))
        self.label_dmh.setText(_translate("mainWindow", "代码行："))
        self.label_kh.setText(_translate("mainWindow", "空 行："))
        self.label_zsh.setText(_translate("mainWindow", "注释行："))
