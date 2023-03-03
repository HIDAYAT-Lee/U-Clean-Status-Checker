# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(907, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_ExitProgram = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.pushButton_ExitProgram.setFont(font)
        self.pushButton_ExitProgram.setObjectName("pushButton_ExitProgram")
        self.gridLayout.addWidget(self.pushButton_ExitProgram, 11, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_About = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.pushButton_About.setFont(font)
        self.pushButton_About.setObjectName("pushButton_About")
        self.gridLayout.addWidget(self.pushButton_About, 11, 1, 1, 1)
        self.pushButton_UploadData = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.pushButton_UploadData.setFont(font)
        self.pushButton_UploadData.setObjectName("pushButton_UploadData")
        self.gridLayout.addWidget(self.pushButton_UploadData, 8, 2, 1, 1)
        self.comboBox_SideSelect = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.comboBox_SideSelect.setFont(font)
        self.comboBox_SideSelect.setObjectName("comboBox_SideSelect")
        self.comboBox_SideSelect.addItem("")
        self.comboBox_SideSelect.addItem("")
        self.gridLayout.addWidget(self.comboBox_SideSelect, 6, 2, 1, 1)
        self.pushButton_StartCheck = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.pushButton_StartCheck.setFont(font)
        self.pushButton_StartCheck.setObjectName("pushButton_StartCheck")
        self.gridLayout.addWidget(self.pushButton_StartCheck, 8, 1, 1, 1)
        self.comboBox_BuildingSelect = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.comboBox_BuildingSelect.setFont(font)
        self.comboBox_BuildingSelect.setObjectName("comboBox_BuildingSelect")
        self.comboBox_BuildingSelect.addItem("")
        self.gridLayout.addWidget(self.comboBox_BuildingSelect, 5, 2, 1, 1)
        self.textBrowser_ShowResult = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_ShowResult.setObjectName("textBrowser_ShowResult")
        self.gridLayout.addWidget(self.textBrowser_ShowResult, 12, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_StartCheck.clicked.connect(MainWindow.StartCheck)
        self.pushButton_ExitProgram.clicked.connect(MainWindow.ExitProgram)
        self.pushButton_UploadData.clicked.connect(MainWindow.UploadData)
        self.pushButton_About.clicked.connect(MainWindow.AboutProgram)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "For SCNU"))
        self.pushButton_ExitProgram.setText(_translate("MainWindow", "退出程序"))
        self.label_2.setText(_translate("MainWindow", "选择宿舍楼:"))
        self.label_3.setText(_translate("MainWindow", "选择水控端:"))
        self.pushButton_About.setText(_translate("MainWindow", "关于程序"))
        self.pushButton_UploadData.setText(_translate("MainWindow", "上传数据"))
        self.comboBox_SideSelect.setItemText(0, _translate("MainWindow", "兆基"))
        self.comboBox_SideSelect.setItemText(1, _translate("MainWindow", "常工"))
        self.pushButton_StartCheck.setText(_translate("MainWindow", "开始查询"))
        self.comboBox_BuildingSelect.setItemText(0, _translate("MainWindow", "东十九"))
        self.label.setText(_translate("MainWindow", "U净洗衣机状态查询器"))
