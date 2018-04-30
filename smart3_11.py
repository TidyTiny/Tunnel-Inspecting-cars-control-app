# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smart3_0.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1528, 999)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../social_round_rss_128px_1196635_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 90, 1411, 871))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setStyleSheet("QTabWidget::pane{\n"
"    border:none;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 30))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 1371, 521))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(150, 250, 1141, 21))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(-1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(150, 260, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(210, 260, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(270, 260, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(330, 260, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(390, 260, 16, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(450, 260, 16, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(510, 260, 16, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(570, 260, 16, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(630, 260, 16, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(690, 260, 16, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(750, 260, 16, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(810, 260, 16, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(870, 260, 16, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(930, 260, 16, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(990, 260, 21, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(1050, 260, 20, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(1110, 260, 21, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(1170, 260, 16, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(1230, 260, 16, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(1290, 260, 21, 16))
        self.label_25.setObjectName("label_25")
        self.label_38 = QtWidgets.QLabel(self.groupBox)
        self.label_38.setGeometry(QtCore.QRect(60, 85, 72, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox)
        self.label_39.setGeometry(QtCore.QRect(60, 335, 72, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(150, 130, 1141, 31))
        self.label_3.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setText("")
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(150, 370, 1141, 31))
        self.label_4.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.groupBox)
        self.quickWidget.setGeometry(QtCore.QRect(-240, 770, 300, 200))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.line_28 = QtWidgets.QFrame(self.groupBox)
        self.line_28.setGeometry(QtCore.QRect(140, 80, 21, 361))
        self.line_28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.groupBox)
        self.line_29.setGeometry(QtCore.QRect(200, 80, 21, 361))
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_30 = QtWidgets.QFrame(self.groupBox)
        self.line_30.setGeometry(QtCore.QRect(260, 80, 21, 361))
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setObjectName("line_30")
        self.line_31 = QtWidgets.QFrame(self.groupBox)
        self.line_31.setGeometry(QtCore.QRect(320, 80, 21, 361))
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setObjectName("line_31")
        self.line_32 = QtWidgets.QFrame(self.groupBox)
        self.line_32.setGeometry(QtCore.QRect(380, 80, 21, 361))
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_32.setObjectName("line_32")
        self.line_33 = QtWidgets.QFrame(self.groupBox)
        self.line_33.setGeometry(QtCore.QRect(440, 80, 21, 361))
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_33.setObjectName("line_33")
        self.line_34 = QtWidgets.QFrame(self.groupBox)
        self.line_34.setGeometry(QtCore.QRect(500, 80, 21, 361))
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_34.setObjectName("line_34")
        self.line_35 = QtWidgets.QFrame(self.groupBox)
        self.line_35.setGeometry(QtCore.QRect(560, 80, 21, 361))
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_35.setObjectName("line_35")
        self.line_36 = QtWidgets.QFrame(self.groupBox)
        self.line_36.setGeometry(QtCore.QRect(620, 80, 21, 361))
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_36.setObjectName("line_36")
        self.line_37 = QtWidgets.QFrame(self.groupBox)
        self.line_37.setGeometry(QtCore.QRect(680, 80, 21, 361))
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_37.setObjectName("line_37")
        self.line_38 = QtWidgets.QFrame(self.groupBox)
        self.line_38.setGeometry(QtCore.QRect(740, 80, 21, 361))
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_38.setObjectName("line_38")
        self.line_39 = QtWidgets.QFrame(self.groupBox)
        self.line_39.setGeometry(QtCore.QRect(800, 80, 21, 361))
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_39.setObjectName("line_39")
        self.line_40 = QtWidgets.QFrame(self.groupBox)
        self.line_40.setGeometry(QtCore.QRect(860, 80, 21, 361))
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_40.setObjectName("line_40")
        self.line_41 = QtWidgets.QFrame(self.groupBox)
        self.line_41.setGeometry(QtCore.QRect(920, 80, 21, 361))
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_41.setObjectName("line_41")
        self.line_42 = QtWidgets.QFrame(self.groupBox)
        self.line_42.setGeometry(QtCore.QRect(980, 80, 21, 361))
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_42.setObjectName("line_42")
        self.line_43 = QtWidgets.QFrame(self.groupBox)
        self.line_43.setGeometry(QtCore.QRect(1040, 80, 21, 361))
        self.line_43.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_43.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_43.setObjectName("line_43")
        self.line_44 = QtWidgets.QFrame(self.groupBox)
        self.line_44.setGeometry(QtCore.QRect(1100, 80, 21, 361))
        self.line_44.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_44.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_44.setObjectName("line_44")
        self.line_45 = QtWidgets.QFrame(self.groupBox)
        self.line_45.setGeometry(QtCore.QRect(1160, 80, 21, 361))
        self.line_45.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_45.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_45.setObjectName("line_45")
        self.line_46 = QtWidgets.QFrame(self.groupBox)
        self.line_46.setGeometry(QtCore.QRect(1220, 80, 21, 361))
        self.line_46.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_46.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_46.setObjectName("line_46")
        self.line_47 = QtWidgets.QFrame(self.groupBox)
        self.line_47.setGeometry(QtCore.QRect(1280, 80, 21, 361))
        self.line_47.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_47.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_47.setObjectName("line_47")
        self.line_4 = QtWidgets.QFrame(self.groupBox)
        self.line_4.setGeometry(QtCore.QRect(150, 70, 1141, 21))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setGeometry(QtCore.QRect(150, 190, 1141, 21))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_7 = QtWidgets.QFrame(self.groupBox)
        self.line_7.setGeometry(QtCore.QRect(150, 310, 1141, 21))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.line_9 = QtWidgets.QFrame(self.groupBox)
        self.line_9.setGeometry(QtCore.QRect(150, 430, 1141, 21))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(150, 100, 41, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_33.setObjectName("label_33")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 20, 41, 41))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/bullet-1-l-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("icon/bullet-1-w-lb.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_58 = QtWidgets.QLabel(self.frame)
        self.label_58.setGeometry(QtCore.QRect(0, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.frame)
        self.label_59.setGeometry(QtCore.QRect(15, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.frame)
        self.label_60.setGeometry(QtCore.QRect(30, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_60.setObjectName("label_60")
        self.label_91 = QtWidgets.QLabel(self.frame)
        self.label_91.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.label_91.setObjectName("label_91")
        self.label_95 = QtWidgets.QLabel(self.frame)
        self.label_95.setGeometry(QtCore.QRect(0, 76, 41, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_95.setFont(font)
        self.label_95.setAlignment(QtCore.Qt.AlignCenter)
        self.label_95.setObjectName("label_95")
        self.label_91.raise_()
        self.label_33.raise_()
        self.pushButton_3.raise_()
        self.label_58.raise_()
        self.label_59.raise_()
        self.label_60.raise_()
        self.label_95.raise_()
        self.label_42 = QtWidgets.QLabel(self.groupBox)
        self.label_42.setGeometry(QtCore.QRect(10, 370, 131, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox)
        self.label_43.setGeometry(QtCore.QRect(10, 120, 131, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setGeometry(QtCore.QRect(470, 100, 41, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_34 = QtWidgets.QLabel(self.frame_2)
        self.label_34.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_34.setObjectName("label_34")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 20, 41, 41))
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/bullet-2-l-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("icon/bullet-2-w-lb.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_61 = QtWidgets.QLabel(self.frame_2)
        self.label_61.setGeometry(QtCore.QRect(0, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.frame_2)
        self.label_62.setGeometry(QtCore.QRect(15, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_62.setObjectName("label_62")
        self.label_75 = QtWidgets.QLabel(self.frame_2)
        self.label_75.setGeometry(QtCore.QRect(30, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_75.setObjectName("label_75")
        self.label_90 = QtWidgets.QLabel(self.frame_2)
        self.label_90.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.label_90.setObjectName("label_90")
        self.label_96 = QtWidgets.QLabel(self.frame_2)
        self.label_96.setGeometry(QtCore.QRect(0, 76, 41, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_96.setFont(font)
        self.label_96.setAlignment(QtCore.Qt.AlignCenter)
        self.label_96.setObjectName("label_96")
        self.label_90.raise_()
        self.label_34.raise_()
        self.pushButton_4.raise_()
        self.label_61.raise_()
        self.label_62.raise_()
        self.label_75.raise_()
        self.label_96.raise_()
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setGeometry(QtCore.QRect(540, 100, 41, 101))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_35 = QtWidgets.QLabel(self.frame_3)
        self.label_35.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_35.setObjectName("label_35")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 20, 41, 41))
        self.pushButton_10.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/bullet-3-l-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_76 = QtWidgets.QLabel(self.frame_3)
        self.label_76.setGeometry(QtCore.QRect(0, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.frame_3)
        self.label_77.setGeometry(QtCore.QRect(15, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_77.setFont(font)
        self.label_77.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(self.frame_3)
        self.label_78.setGeometry(QtCore.QRect(30, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_78.setFont(font)
        self.label_78.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_78.setObjectName("label_78")
        self.label_89 = QtWidgets.QLabel(self.frame_3)
        self.label_89.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.label_89.setObjectName("label_89")
        self.label_97 = QtWidgets.QLabel(self.frame_3)
        self.label_97.setGeometry(QtCore.QRect(0, 76, 41, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_97.setFont(font)
        self.label_97.setAlignment(QtCore.Qt.AlignCenter)
        self.label_97.setObjectName("label_97")
        self.label_89.raise_()
        self.label_35.raise_()
        self.pushButton_10.raise_()
        self.label_77.raise_()
        self.label_78.raise_()
        self.label_76.raise_()
        self.label_97.raise_()
        self.frame_4 = QtWidgets.QFrame(self.groupBox)
        self.frame_4.setGeometry(QtCore.QRect(10, 390, 41, 101))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_36 = QtWidgets.QLabel(self.frame_4)
        self.label_36.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_36.setObjectName("label_36")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_15.setGeometry(QtCore.QRect(0, 20, 41, 41))
        self.pushButton_15.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/bullet-4-l-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("icon/bullet-4-w-lb.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_15.setIcon(icon4)
        self.pushButton_15.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_15.setFlat(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_79 = QtWidgets.QLabel(self.frame_4)
        self.label_79.setGeometry(QtCore.QRect(0, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.frame_4)
        self.label_80.setGeometry(QtCore.QRect(15, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.frame_4)
        self.label_81.setGeometry(QtCore.QRect(30, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_81.setObjectName("label_81")
        self.label_92 = QtWidgets.QLabel(self.frame_4)
        self.label_92.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.label_92.setObjectName("label_92")
        self.label_98 = QtWidgets.QLabel(self.frame_4)
        self.label_98.setGeometry(QtCore.QRect(0, 76, 41, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_98.setFont(font)
        self.label_98.setAlignment(QtCore.Qt.AlignCenter)
        self.label_98.setObjectName("label_98")
        self.label_92.raise_()
        self.label_36.raise_()
        self.pushButton_15.raise_()
        self.label_79.raise_()
        self.label_80.raise_()
        self.label_81.raise_()
        self.label_98.raise_()
        self.frame_6 = QtWidgets.QFrame(self.groupBox)
        self.frame_6.setGeometry(QtCore.QRect(110, 390, 41, 101))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_85 = QtWidgets.QLabel(self.frame_6)
        self.label_85.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_85.setFont(font)
        self.label_85.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_85.setObjectName("label_85")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 20, 41, 41))
        self.pushButton_17.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/bullet-6-l-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("icon/bullet-6-w-lb.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_17.setFlat(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_86 = QtWidgets.QLabel(self.frame_6)
        self.label_86.setGeometry(QtCore.QRect(0, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.frame_6)
        self.label_87.setGeometry(QtCore.QRect(15, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.frame_6)
        self.label_88.setGeometry(QtCore.QRect(30, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_88.setObjectName("label_88")
        self.label_94 = QtWidgets.QLabel(self.frame_6)
        self.label_94.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.label_94.setObjectName("label_94")
        self.label_100 = QtWidgets.QLabel(self.frame_6)
        self.label_100.setGeometry(QtCore.QRect(0, 76, 41, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_100.setFont(font)
        self.label_100.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100.setObjectName("label_100")
        self.label_94.raise_()
        self.label_85.raise_()
        self.pushButton_17.raise_()
        self.label_86.raise_()
        self.label_87.raise_()
        self.label_88.raise_()
        self.label_100.raise_()
        self.frame_5 = QtWidgets.QFrame(self.groupBox)
        self.frame_5.setGeometry(QtCore.QRect(60, 390, 41, 101))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_37 = QtWidgets.QLabel(self.frame_5)
        self.label_37.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_37.setObjectName("label_37")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_16.setGeometry(QtCore.QRect(0, 20, 41, 41))
        self.pushButton_16.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/bullet-5-l-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("icon/bullet-5-w-lb.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_16.setIcon(icon6)
        self.pushButton_16.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_16.setFlat(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_82 = QtWidgets.QLabel(self.frame_5)
        self.label_82.setGeometry(QtCore.QRect(0, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.frame_5)
        self.label_83.setGeometry(QtCore.QRect(15, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.frame_5)
        self.label_84.setGeometry(QtCore.QRect(30, 65, 12, 12))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setStyleSheet("color: rgb(0, 213, 0);\n"
"background-color: rgb(0, 213, 0);")
        self.label_84.setObjectName("label_84")
        self.label_93 = QtWidgets.QLabel(self.frame_5)
        self.label_93.setGeometry(QtCore.QRect(0, 10, 40, 5))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_93.setFont(font)
        self.label_93.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.label_93.setObjectName("label_93")
        self.label_99 = QtWidgets.QLabel(self.frame_5)
        self.label_99.setGeometry(QtCore.QRect(0, 76, 41, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_99.setFont(font)
        self.label_99.setAlignment(QtCore.Qt.AlignCenter)
        self.label_99.setObjectName("label_99")
        self.label_93.raise_()
        self.label_37.raise_()
        self.pushButton_16.raise_()
        self.label_82.raise_()
        self.label_83.raise_()
        self.label_84.raise_()
        self.label_99.raise_()
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(980, 10, 311, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 34, 111, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_24.setGeometry(QtCore.QRect(170, 34, 111, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_3.raise_()
        self.label_4.raise_()
        self.line_46.raise_()
        self.line_45.raise_()
        self.line_44.raise_()
        self.line_43.raise_()
        self.line_42.raise_()
        self.line_41.raise_()
        self.line_40.raise_()
        self.line_39.raise_()
        self.line_38.raise_()
        self.line_37.raise_()
        self.line_36.raise_()
        self.line_35.raise_()
        self.line_34.raise_()
        self.line_33.raise_()
        self.line_32.raise_()
        self.line_31.raise_()
        self.line_30.raise_()
        self.line_29.raise_()
        self.line_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.quickWidget.raise_()
        self.line_28.raise_()
        self.line_47.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_7.raise_()
        self.line_9.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.groupBox_3.raise_()
        self.frame.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(780, 550, 611, 291))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_40 = QtWidgets.QLabel(self.groupBox_2)
        self.label_40.setGeometry(QtCore.QRect(40, 30, 72, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_2)
        self.label_41.setGeometry(QtCore.QRect(40, 150, 72, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(120, 60, 31, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgb(123, 140, 234);\n"
"    text-align: center;\n"
"}\n"
"")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(120, 180, 31, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(123, 140, 234);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(120, 90, 451, 21))
        self.label_26.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(120, 180, 451, 21))
        self.label_27.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(120, 60, 451, 21))
        self.label_28.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_52 = QtWidgets.QLabel(self.groupBox_2)
        self.label_52.setGeometry(QtCore.QRect(120, 120, 451, 21))
        self.label_52.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_52.setText("")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.groupBox_2)
        self.label_53.setGeometry(QtCore.QRect(10, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_2)
        self.label_54.setGeometry(QtCore.QRect(10, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.groupBox_2)
        self.label_55.setGeometry(QtCore.QRect(10, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.groupBox_2)
        self.label_56.setGeometry(QtCore.QRect(120, 210, 451, 21))
        self.label_56.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.groupBox_2)
        self.label_57.setGeometry(QtCore.QRect(120, 240, 451, 21))
        self.label_57.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_57.setText("")
        self.label_57.setObjectName("label_57")
        self.label_64 = QtWidgets.QLabel(self.groupBox_2)
        self.label_64.setGeometry(QtCore.QRect(10, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.groupBox_2)
        self.label_65.setGeometry(QtCore.QRect(10, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.groupBox_2)
        self.label_66.setGeometry(QtCore.QRect(10, 240, 91, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.groupBox_2)
        self.label_67.setGeometry(QtCore.QRect(120, 90, 31, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_67.setFont(font)
        self.label_67.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_67.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_67.setStyleSheet("background-color: rgb(123, 170, 234);")
        self.label_67.setTextFormat(QtCore.Qt.AutoText)
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.groupBox_2)
        self.label_68.setGeometry(QtCore.QRect(120, 120, 31, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_68.setFont(font)
        self.label_68.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_68.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_68.setStyleSheet("background-color: rgb(123, 200, 234);")
        self.label_68.setTextFormat(QtCore.Qt.AutoText)
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.groupBox_2)
        self.label_69.setGeometry(QtCore.QRect(120, 210, 31, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_69.setFont(font)
        self.label_69.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_69.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_69.setStyleSheet("background-color: rgb(123, 170, 234);")
        self.label_69.setTextFormat(QtCore.Qt.AutoText)
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.groupBox_2)
        self.label_70.setGeometry(QtCore.QRect(120, 240, 31, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_70.setFont(font)
        self.label_70.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_70.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_70.setStyleSheet("background-color: rgb(123, 200, 234);")
        self.label_70.setTextFormat(QtCore.Qt.AutoText)
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.label_28.raise_()
        self.label_27.raise_()
        self.label_26.raise_()
        self.label_40.raise_()
        self.label_41.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_53.raise_()
        self.label_54.raise_()
        self.label_55.raise_()
        self.label_64.raise_()
        self.label_65.raise_()
        self.label_66.raise_()
        self.label_52.raise_()
        self.label_56.raise_()
        self.label_57.raise_()
        self.label_67.raise_()
        self.label_68.raise_()
        self.label_69.raise_()
        self.label_70.raise_()
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(720, 870, 641, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 550, 271, 291))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 231, 28))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: qconicalgradient(cx:0.5, cy:0.522909, angle:179.9, stop:0.494318 rgba(214, 214, 214, 255), stop:0.5 rgba(236, 236, 236, 255));\n"
"border: 1px solid rgb(124, 124, 124);\n"
"border-radius:5px;\n"
"}\n"
"selection-color: rgb(123, 191, 234);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/power_button_128px_1206378_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.groupBox_4)
        self.tabWidget_3.setGeometry(QtCore.QRect(20, 30, 231, 191))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setStyleSheet("QTabWidget::pane{\n"
"    border:none;\n"
"}\n"
"QTabWidget::tab-bar{\n"
"        alignment:left;\n"
"}\n"
"QTabBar::tab{\n"
"    color:black;\n"
"    min-width:10ex;\n"
"    min-height:5ex;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    background-color: rgb(220, 220, 220, 100);\n"
"}\n"
"")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.layoutWidget = QtWidgets.QWidget(self.tab_7)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 231, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_5.addWidget(self.label_29)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_6.addWidget(self.label_30)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_31 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_7.addWidget(self.label_31)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_32 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_8.addWidget(self.label_32)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_8)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 231, 141))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_71 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_9.addWidget(self.label_71)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_5.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_5.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_72 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_10.addWidget(self.label_72)
        self.comboBox_6 = QtWidgets.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_73 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.horizontalLayout_11.addWidget(self.label_73)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_74 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.horizontalLayout_12.addWidget(self.label_74)
        self.comboBox_8 = QtWidgets.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_25.setGeometry(QtCore.QRect(80, 280, 93, 28))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_26.setGeometry(QtCore.QRect(180, 280, 93, 28))
        self.pushButton_26.setObjectName("pushButton_26")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(310, 550, 451, 291))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"")
        self.groupBox_5.setObjectName("groupBox_5")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 431, 261))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(76, 190, 243))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 1, item)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setGeometry(QtCore.QRect(310, 59, 121, 21))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(123, 191, 234, 150);\n"
"    width: 20px;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_3.setGeometry(QtCore.QRect(310, 132, 121, 21))
        self.progressBar_3.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(123, 191, 234, 150);\n"
"    width: 20px;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_4.setGeometry(QtCore.QRect(310, 169, 121, 20))
        self.progressBar_4.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(123, 191, 234, 150);\n"
"    width: 20px;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setInvertedAppearance(False)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_5.setGeometry(QtCore.QRect(310, 205, 121, 21))
        self.progressBar_5.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(123, 191, 234, 150);\n"
"    width: 20px;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_2.setGeometry(QtCore.QRect(310, 96, 121, 21))
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(123, 191, 234, 150);\n"
"    width: 20px;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_6 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_6.setGeometry(QtCore.QRect(310, 243, 121, 20))
        self.progressBar_6.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(123, 191, 234, 150);\n"
"    width: 20px;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setObjectName("progressBar_6")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_18.setGeometry(QtCore.QRect(310, 57, 121, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_19.setGeometry(QtCore.QRect(310, 97, 121, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_20.setGeometry(QtCore.QRect(310, 130, 121, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_21.setGeometry(QtCore.QRect(310, 167, 121, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_22.setGeometry(QtCore.QRect(310, 207, 121, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_23.setGeometry(QtCore.QRect(310, 240, 121, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.groupBox_2.raise_()
        self.textBrowser.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.groupBox.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(123, 191, 234);")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.label_45.setStyleSheet("background-color: rgb(123, 191, 234);")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(0, -10, 71, 971))
        self.label_46.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.label_63 = QtWidgets.QLabel(self.centralwidget)
        self.label_63.setGeometry(QtCore.QRect(60, -30, 1481, 971))
        self.label_63.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_63.setText("")
        self.label_63.setObjectName("label_63")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 1541, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("QTabWidget::pane{\n"
"    border:none;\n"
"}\n"
"QTabWidget::tab-bar{\n"
"        alignment:right;\n"
"}\n"
"QTabBar::tab{\n"
"    background:rgb(123,191,234,255);\n"
"    color:black;\n"
"    min-width:35ex;\n"
"    min-height:13ex;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    background:rgb(220,220,220, 100);\n"
"}\n"
"")
        self.tabWidget_2.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_47 = QtWidgets.QLabel(self.tab_3)
        self.label_47.setGeometry(QtCore.QRect(-250, 0, 1791, 41))
        self.label_47.setStyleSheet("background-color: rgb(220,220,220,200);")
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(1180, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(1300, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(1420, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/social_round_blogger_128px_1196623_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_3, icon8, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_48 = QtWidgets.QLabel(self.tab_5)
        self.label_48.setGeometry(QtCore.QRect(0, 0, 1541, 41))
        self.label_48.setStyleSheet("background-color: rgb(220,220,220,100);")
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setGeometry(QtCore.QRect(1300, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_9.setGeometry(QtCore.QRect(1420, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_11.setGeometry(QtCore.QRect(1180, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/social_round_feedly_128px_1196629_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_5, icon9, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_49 = QtWidgets.QLabel(self.tab_4)
        self.label_49.setGeometry(QtCore.QRect(-30, 0, 1581, 41))
        self.label_49.setStyleSheet("background-color: rgb(220,220,220,100);")
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_12.setGeometry(QtCore.QRect(1420, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_13.setGeometry(QtCore.QRect(1300, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/social_round_buffer_128px_1196624_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_4, icon10, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_50 = QtWidgets.QLabel(self.tab_6)
        self.label_50.setGeometry(QtCore.QRect(-250, -10, 1791, 51))
        self.label_50.setStyleSheet("background-color: rgb(220,220,220,100);")
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_14.setGeometry(QtCore.QRect(1420, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/social_round_flickr_128px_1196630_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_6, icon11, "")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(40, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("")
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap("icon/social_round_rss_128px_1196635_easyicon.net.ico"))
        self.label_44.setScaledContents(True)
        self.label_44.setObjectName("label_44")
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setGeometry(QtCore.QRect(0, 0, 991, 52))
        self.label_51.setStyleSheet("background-color: rgb(123, 191, 234);")
        self.label_51.setText("")
        self.label_51.setIndent(0)
        self.label_51.setObjectName("label_51")
        self.label_63.raise_()
        self.label_46.raise_()
        self.tabWidget.raise_()
        self.label_45.raise_()
        self.tabWidget_2.raise_()
        self.label_51.raise_()
        self.label_5.raise_()
        self.label_44.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1528, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "隧道智能巡检控制系统"))
        MainWindow.setStatusTip(_translate("MainWindow", "欢迎使用！当前版本：3.0"))
        self.groupBox.setToolTip(_translate("MainWindow", "这里你可以直观地查看目前各个小车的实时位置"))
        self.groupBox.setTitle(_translate("MainWindow", "隧道俯视图"))
        self.line_2.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_6.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_7.setText(_translate("MainWindow", "1"))
        self.label_8.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_8.setText(_translate("MainWindow", "2"))
        self.label_9.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_9.setText(_translate("MainWindow", "3"))
        self.label_10.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_10.setText(_translate("MainWindow", "4"))
        self.label_11.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_11.setText(_translate("MainWindow", "5"))
        self.label_12.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_12.setText(_translate("MainWindow", "6"))
        self.label_13.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_13.setText(_translate("MainWindow", "7"))
        self.label_14.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_14.setText(_translate("MainWindow", "8"))
        self.label_15.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_15.setText(_translate("MainWindow", "9"))
        self.label_16.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_16.setText(_translate("MainWindow", "10"))
        self.label_17.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_17.setText(_translate("MainWindow", "11"))
        self.label_18.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_18.setText(_translate("MainWindow", "12"))
        self.label_19.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_19.setText(_translate("MainWindow", "13"))
        self.label_20.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_20.setText(_translate("MainWindow", "14"))
        self.label_21.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_21.setText(_translate("MainWindow", "15"))
        self.label_22.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_22.setText(_translate("MainWindow", "16"))
        self.label_23.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_23.setText(_translate("MainWindow", "17"))
        self.label_24.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_24.setText(_translate("MainWindow", "18"))
        self.label_25.setToolTip(_translate("MainWindow", "这是隧道的坐标图，单位为km"))
        self.label_25.setText(_translate("MainWindow", "19"))
        self.label_38.setText(_translate("MainWindow", "1号单轨："))
        self.label_39.setText(_translate("MainWindow", "2号单轨："))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "点击查看1号车的具体状态"))
        self.label_58.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表安全行驶，红灯代表发生故障</p></body></html>"))
        self.label_58.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_59.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行编组，红灯表示已编组</p></body></html>"))
        self.label_59.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_60.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行翻越，红灯代表正在进行翻越</p></body></html>"))
        self.label_60.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_91.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_95.setText(_translate("MainWindow", "正常"))
        self.label_42.setText(_translate("MainWindow", "2号单轨空闲车："))
        self.label_43.setText(_translate("MainWindow", "1号单轨空闲车："))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "点击查看1号车的具体状态"))
        self.label_61.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表安全行驶，红灯代表发生故障</p></body></html>"))
        self.label_61.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_62.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行编组，红灯表示已编组</p></body></html>"))
        self.label_62.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_75.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行翻越，红灯代表正在进行翻越</p></body></html>"))
        self.label_75.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_90.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_96.setText(_translate("MainWindow", "正常"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "点击查看1号车的具体状态"))
        self.label_76.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表安全行驶，红灯代表发生故障</p></body></html>"))
        self.label_76.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_77.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行编组，红灯表示已编组</p></body></html>"))
        self.label_77.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_78.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行翻越，红灯代表正在进行翻越</p></body></html>"))
        self.label_78.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_89.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_97.setText(_translate("MainWindow", "正常"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_15.setToolTip(_translate("MainWindow", "点击查看1号车的具体状态"))
        self.label_79.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表安全行驶，红灯代表发生故障</p></body></html>"))
        self.label_79.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_80.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行编组，红灯表示已编组</p></body></html>"))
        self.label_80.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_81.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行翻越，红灯代表正在进行翻越</p></body></html>"))
        self.label_81.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_92.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_98.setText(_translate("MainWindow", "正常"))
        self.label_85.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_17.setToolTip(_translate("MainWindow", "点击查看1号车的具体状态"))
        self.label_86.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表安全行驶，红灯代表发生故障</p></body></html>"))
        self.label_86.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_87.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行编组，红灯表示已编组</p></body></html>"))
        self.label_87.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_88.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行翻越，红灯代表正在进行翻越</p></body></html>"))
        self.label_88.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_94.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_100.setText(_translate("MainWindow", "正常"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_16.setToolTip(_translate("MainWindow", "点击查看1号车的具体状态"))
        self.label_82.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表安全行驶，红灯代表发生故障</p></body></html>"))
        self.label_82.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_83.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行编组，红灯表示已编组</p></body></html>"))
        self.label_83.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_84.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>绿灯代表没有进行翻越，红灯代表正在进行翻越</p></body></html>"))
        self.label_84.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_93.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_99.setText(_translate("MainWindow", "正常"))
        self.groupBox_3.setTitle(_translate("MainWindow", "演示专用"))
        self.pushButton_6.setText(_translate("MainWindow", "编组"))
        self.pushButton_24.setText(_translate("MainWindow", "翻越"))
        self.groupBox_2.setToolTip(_translate("MainWindow", "这里会记录检测的结果并直观地反映出来"))
        self.groupBox_2.setTitle(_translate("MainWindow", "隧道状态总览"))
        self.label_40.setText(_translate("MainWindow", "1号单轨："))
        self.label_41.setText(_translate("MainWindow", "2号单轨："))
        self.label.setToolTip(_translate("MainWindow", "已检测"))
        self.label.setText(_translate("MainWindow", "安全"))
        self.label_2.setToolTip(_translate("MainWindow", "已检测"))
        self.label_2.setText(_translate("MainWindow", "安全"))
        self.label_53.setText(_translate("MainWindow", "项目1状态："))
        self.label_54.setText(_translate("MainWindow", "项目2状态："))
        self.label_55.setText(_translate("MainWindow", "项目3状态："))
        self.label_64.setText(_translate("MainWindow", "项目1状态："))
        self.label_65.setText(_translate("MainWindow", "项目2状态："))
        self.label_66.setText(_translate("MainWindow", "项目3状态："))
        self.label_67.setToolTip(_translate("MainWindow", "已检测"))
        self.label_67.setText(_translate("MainWindow", "安全"))
        self.label_68.setToolTip(_translate("MainWindow", "已检测"))
        self.label_68.setText(_translate("MainWindow", "安全"))
        self.label_69.setToolTip(_translate("MainWindow", "已检测"))
        self.label_69.setText(_translate("MainWindow", "安全"))
        self.label_70.setToolTip(_translate("MainWindow", "已检测"))
        self.label_70.setText(_translate("MainWindow", "安全"))
        self.textBrowser.setToolTip(_translate("MainWindow", "这里讲记录并显示检测的具体数据"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "任务分配"))
        self.pushButton.setToolTip(_translate("MainWindow", "这个按钮并没有实际功能，而是用于软件的测试。"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>这个按钮并没有什么实际的作用，用于软件功能的测试。</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "显示三维仿真"))
        self.label_29.setText(_translate("MainWindow", "检测项目1："))
        self.comboBox.setToolTip(_translate("MainWindow", "请分配任务"))
        self.comboBox.setItemText(0, _translate("MainWindow", "4号车"))
        self.comboBox.setItemText(1, _translate("MainWindow", "5号车"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6号车"))
        self.label_30.setText(_translate("MainWindow", "检测项目2："))
        self.comboBox_2.setToolTip(_translate("MainWindow", "请分配任务"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "4号车"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "5号车"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "6号车"))
        self.label_31.setText(_translate("MainWindow", "检测项目3："))
        self.comboBox_3.setToolTip(_translate("MainWindow", "请分配任务"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "4号车"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "5号车"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "6号车"))
        self.label_32.setText(_translate("MainWindow", "视频监控："))
        self.comboBox_4.setToolTip(_translate("MainWindow", "请分配任务"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "4号车"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "5号车"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "6号车"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "2号单轨"))
        self.label_71.setText(_translate("MainWindow", "检测项目1："))
        self.comboBox_5.setToolTip(_translate("MainWindow", "请分配任务"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "1号车"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "2号车"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "3号车"))
        self.label_72.setText(_translate("MainWindow", "检测项目2："))
        self.comboBox_6.setToolTip(_translate("MainWindow", "请分配任务"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "1号车"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "2号车"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "3号车"))
        self.label_73.setText(_translate("MainWindow", "检测项目3："))
        self.comboBox_7.setToolTip(_translate("MainWindow", "请分配任务"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "1号车"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "2号车"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "3号车"))
        self.label_74.setText(_translate("MainWindow", "视频监控："))
        self.comboBox_8.setToolTip(_translate("MainWindow", "请分配任务"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "1号车"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "2号车"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "3号车"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "1号单轨"))
        self.pushButton_25.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_26.setText(_translate("MainWindow", "PushButton"))
        self.groupBox_5.setTitle(_translate("MainWindow", "车组状态"))
        self.tableWidget.setToolTip(_translate("MainWindow", "这里你将直观地看到各个任务的分配以及执行情况"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1号车"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2号车"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3号车"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4号车"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5号车"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6号车"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "状态"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "任务"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "手动制动"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.progressBar.setToolTip(_translate("MainWindow", "这里反映了项目的进度"))
        self.progressBar_3.setToolTip(_translate("MainWindow", "这里反映了项目的进度"))
        self.progressBar_4.setToolTip(_translate("MainWindow", "这里反映了项目的进度"))
        self.progressBar_5.setToolTip(_translate("MainWindow", "这里反映了项目的进度"))
        self.progressBar_2.setToolTip(_translate("MainWindow", "这里反映了项目的进度"))
        self.progressBar_6.setToolTip(_translate("MainWindow", "这里反映了项目的进度"))
        self.pushButton_18.setText(_translate("MainWindow", "停止"))
        self.pushButton_19.setText(_translate("MainWindow", "停止"))
        self.pushButton_20.setText(_translate("MainWindow", "停止"))
        self.pushButton_21.setText(_translate("MainWindow", "停止"))
        self.pushButton_22.setText(_translate("MainWindow", "停止"))
        self.pushButton_23.setText(_translate("MainWindow", "停止"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "主界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "辅助界面"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">隧道智能巡检</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "设置"))
        self.pushButton_5.setText(_translate("MainWindow", "布局"))
        self.pushButton_7.setText(_translate("MainWindow", "退出"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "菜单"))
        self.pushButton_8.setText(_translate("MainWindow", "项目2分析"))
        self.pushButton_9.setText(_translate("MainWindow", "项目3分析"))
        self.pushButton_11.setText(_translate("MainWindow", "项目1分析"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "分析"))
        self.pushButton_12.setText(_translate("MainWindow", "视频录像"))
        self.pushButton_13.setText(_translate("MainWindow", "历史数据"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "数据库"))
        self.pushButton_14.setText(_translate("MainWindow", "关于"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "帮助"))

from PyQt5 import QtQuickWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

