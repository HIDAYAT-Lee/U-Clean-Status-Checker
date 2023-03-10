# -*- coding: utf-8 -*-
import sys
import time

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from StatusFetcher import returnStatus
from MachineURL import *
import icon_rc

# 设定全局变量global_result
global_result = ""


class getStatusThread(QThread):
    finished = pyqtSignal()

    def __init__(self, building, side, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.building = building
        self.side = side

    def run(self):
        result = self.msgGenerator()
        # 赋值给全局变量global_result
        global global_result
        global_result = result
        self.finished.emit()

    def msgGenerator(self):
        if self.building == "东十九":
            if self.side == "兆基":
                urlList = D19[0]
                result = self.building + '楼' + self.side + '侧洗衣机状态:\n\n'
                result = result + returnStatus(urlList)
            elif self.side == "常工":
                urlList = D19[1]
                result = self.building + '楼' + self.side + '侧洗衣机状态:\n\n'
                result = result + returnStatus(urlList)
        return result


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
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
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
        self.pushButton_StartCheck.clicked.connect(self.StartCheck)
        self.pushButton_ExitProgram.clicked.connect(self.ExitProgram)
        self.pushButton_UploadData.clicked.connect(self.UploadData)
        self.pushButton_About.clicked.connect(self.AboutProgram)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "For SCNU"))
        self.pushButton_ExitProgram.setText(_translate("MainWindow", "退出程序"))
        self.label_2.setText(_translate("MainWindow", "选择宿舍楼:"))
        self.label_3.setText(_translate("MainWindow", "选择水控端:"))
        self.pushButton_About.setText(_translate("MainWindow", "关于程序"))
        self.pushButton_UploadData.setText(_translate("MainWindow", "协助开发"))
        self.comboBox_SideSelect.setItemText(0, _translate("MainWindow", "兆基"))
        self.comboBox_SideSelect.setItemText(1, _translate("MainWindow", "常工"))
        self.pushButton_StartCheck.setText(_translate("MainWindow", "开始查询"))
        self.comboBox_BuildingSelect.setItemText(0, _translate("MainWindow", "东十九"))
        self.label.setText(_translate("MainWindow", "U净洗衣机状态查询器"))

        # 设置字体为18，华文新魏
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.textBrowser_ShowResult.setFont(font)
        # 设置窗口图标,利用icon_rc.py文件
        MainWindow.setWindowIcon(QtGui.QIcon(':/icon.ico'))
        # 设置窗口标题
        MainWindow.setWindowTitle("U Clean Status Checker")
        self.textBrowser_ShowResult.clear()
        self.textBrowser_ShowResult.setText(
            '本项目GitHub地址:  https://github.com/HIDAYAT-Lee/U-Clean-Status-Checker\n\n如需支持更多宿舍楼的洗衣机，请点击"协助开发"按钮，帮助作者获得必要信息\n\n本程序仅供学习交流使用')

    def StartCheck(self):
        # 按钮变灰
        self.pushButton_StartCheck.setEnabled(False)
        # 改变按钮文字
        self.pushButton_StartCheck.setText("查询中...")
        # 创建线程
        self.thread = getStatusThread(self.comboBox_BuildingSelect.currentText(),
                                      self.comboBox_SideSelect.currentText())
        # 连接信号
        self.thread.finished.connect(self.doneThread)
        self.thread.start()

    def doneThread(self):
        self.pushButton_StartCheck.setEnabled(True)
        self.thread.quit()
        self.thread.wait()
        self.thread.deleteLater()
        self.thread = None
        self.pushButton_StartCheck.setText("开始查询")
        self.textBrowser_ShowResult.setText(global_result)

    def ExitProgram(self):
        sys.exit()

    def UploadData(self):
        # 输出文字到文本框，先清空
        self.textBrowser_ShowResult.clear()
        self.textBrowser_ShowResult.setText(
            "如需支持更多宿舍楼的洗衣机，请协助作者获取对应宿舍楼的洗衣机URL\n\n洗衣机的二维码扫描之后，会得到一串指向这台机器的链接\n\n请前往GitHub提交issue，并附加洗衣机二维码扫描后得到的链接。\n\n请按照以下格式提交:    xx楼xx侧xx层洗衣机:扫码得到的url\n\n如:    东十九楼兆基侧一层洗衣机:http://app.littleswan.com/u_download.html?type=Ujing& uuid=0000000000000A0007555201809040059546\n\n作者将及时更新并提供支持服务")

    def AboutProgram(self):
        # 输出文字到文本框，先清空
        self.textBrowser_ShowResult.clear()
        self.textBrowser_ShowResult.setText(
            '本项目GitHub地址:  https://github.com/HIDAYAT-Lee/U-Clean-Status-Checker\n\n如需支持更多宿舍楼的洗衣机，请点击"协助开发"按钮，帮助作者获得必要信息\n\n本程序仅供学习交流使用')
