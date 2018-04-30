import datetime
import binascii
import serial
import os
import smart3_11
import OpenMySQL
import OpenSmartCars3D
import sys
import time
from PyQt5 import QtCore,QtWidgets,QtGui,QtWebEngineWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QBasicTimer
from PyQt5 import QtQuickWidgets
from PyQt5 import QtWebEngineWidgets
import numpy as np  
import matplotlib.pyplot as plt


# ser = serial.Serial('COM3', 9600)
# 这里定义串口接受函数：

def receive():
    global InputString
    global recv
    while True:
        InputString = ser.inWaiting()
        if InputString != 0:
            data = str(binascii.b2a_hex(ser.read(InputString)))[2:-1]
            if (data.find("fe", 0, len(data)) == 0) and (data.find("ff",  0, len(data)) == (len(data)-2) ):
                if len(data) == 16:
                    if (data[12] == '0') and  (data[13] == '1'):
                        print('hhh')
        time.sleep(0.01)


def control():
    pass


# 这里是定义动画里的“颜色”属性：
class MyLabel(QLabel):
    def __init__(self, text, para):
        super().__init__(text, para)

    def _set_color(self, col):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), col)
        self.setPalette(palette)

    color = pyqtProperty(QColor, fset=_set_color)

# 这里定义帮助界面：


class HelpWindow(QWidget):
    def __init__(self, parent = None):
        super(HelpWindow, self).__init__(parent)
        self.resize(400,200)
        self.setWindowTitle('欢迎来到TidyTiny的帮助')
        self.setWindowIcon(QIcon('icon/person_add_128px_1182113_easyicon.net.ico'))
        self.add_position_layout()

    def add_position_layout(self):
        label = QLabel("当前版本：3.0\n完成时间：2018.3.23\n数据库部分任然比较粗糙，会出现卡顿现象\n点击开始运行时出现短暂卡顿属于正常现象望谅解！",self)
        label.move(40,50)

    def handle_click_help(self):
        if not self.isVisible():
            self.show()


# 定义警告消息的弹出窗口，一共3个：

class Car1message(QWidget):
    def __init__(self, parent = None):
        super(Car1message, self).__init__(parent)
        self.resize(400,150)
        self.setWindowTitle('警告')
        self.setWindowIcon(QIcon('icon/warning.png'))
        self.add_position_layout()

    def add_position_layout(self):
        label = QLabel("1号车已停止运动！",self)
        label.move(100,50)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)

    def handle_click_help(self):
        if not self.isVisible():
            self.show()


class Car2message(QWidget):
    def __init__(self, parent = None):
        super(Car2message, self).__init__(parent)
        self.resize(400,150)
        self.setWindowTitle('警告')
        self.setWindowIcon(QIcon('icon/warning.png'))
        self.add_position_layout()

    def add_position_layout(self):
        label = QLabel("2号车已停止运动！",self)
        label.move(100,50)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)

    def handle_click_help(self):
        if not self.isVisible():
            self.show()


class Car3message(QWidget):
    def __init__(self, parent = None):
        super(Car3message, self).__init__(parent)
        self.resize(400,150)
        self.setWindowTitle('警告')
        self.setWindowIcon(QIcon('icon/warning.png'))
        self.add_position_layout()

    def add_position_layout(self):
        label = QLabel("3号车动力系统损坏！\n已安排1号车救援！",self)
        label.move(100,50)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)

    def handle_click_help(self):
        if not self.isVisible():
            self.show()


# 这里定义每辆小车点击时候的视频监控弹窗：

class Car1(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
 
    def iniUI(self):
        self.setWindowTitle("1号车状态详情")
        self.setWindowIcon(QIcon('icon/access_point_80px_1121181_easyicon.net.ico'))
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(20, 10, 601, 421))
        self.webView.setUrl(QtCore.QUrl('http://www.baidu.com'))
    

class Car2(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
 
    def iniUI(self):
        self.setWindowTitle("2号车状态详情")
        self.setWindowIcon(QIcon('icon/access_point_80px_1121181_easyicon.net.ico'))
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(20, 10, 601, 421))
        self.webView.setUrl(QtCore.QUrl('http://www.baidu.com'))


class Car3(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
 
    def iniUI(self):
        self.setWindowTitle("3号车状态详情")
        self.setWindowIcon(QIcon('icon/access_point_80px_1121181_easyicon.net.ico'))
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(20, 10, 601, 421))
        self.webView.setUrl(QtCore.QUrl('http://www.baidu.com'))


class Car4(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
 
    def iniUI(self):
        self.setWindowTitle("4号车状态详情")
        self.setWindowIcon(QIcon('icon/access_point_80px_1121181_easyicon.net.ico'))
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(20, 10, 601, 421))
        self.webView.setUrl(QtCore.QUrl('http://www.baidu.com'))


class Car5(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
 
    def iniUI(self):
        self.setWindowTitle("5号车状态详情")
        self.setWindowIcon(QIcon('icon/access_point_80px_1121181_easyicon.net.ico'))
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(20, 10, 601, 421))
        self.webView.setUrl(QtCore.QUrl('http://www.baidu.com'))


class Car6(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUI()
 
    def iniUI(self):
        self.setWindowTitle("6号车状态详情")
        self.setWindowIcon(QIcon('icon/access_point_80px_1121181_easyicon.net.ico'))
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(20, 10, 601, 421))
        self.webView.setUrl(QtCore.QUrl('http://www.baidu.com'))


# 这里使用QThread类来进行多线程编程：

class RunThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None, counter_start=0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True

    def run(self):
        while self.counter < 100 and self.is_running ==True:
            time.sleep(0.1)
            self.counter += 1
            print(self.counter)
            self.counter_value.emit(self.counter)

    def stop(self):
        self.is_running = False
        print('线程停止中...')
        self.terminate()


receivethread = RunThread()


class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = smart3_11.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.thread0 = RunThread()
        self.thread = RunThread()
        self.thread2 = RunThread()
        self.thread3 = RunThread()
        self.thread3_1 = RunThread()
        self.thread4 = RunThread()
        self.thread5 = RunThread()
        self.thread6 = RunThread()
        self.ui.thread7 = RunThread()
        self.ui.thread8 = RunThread()
        self.ui.thread9 = RunThread()
        self.ui.thread10 = RunThread()
        self.ui.thread6_2 = RunThread()
        self.ui.thread7_2 = RunThread()
        self.ui.thread8_2 = RunThread()
        self.ui.thread9_2 = RunThread()
        self.ui.thread10_2 = RunThread()
        self.ui.threadt1 = RunThread()
        self.ui.threadt2 = RunThread()
        self.ui.threadt3 = RunThread()
        self.ui.threadt4 = RunThread()
        self.ui.threadt5 = RunThread()
        self.ui.threadt6 = RunThread()
        self.ui.threade1 = RunThread()
        self.ui.threade2 = RunThread()
        self.ui.threade3 = RunThread()
        self.ui.threade4 = RunThread()
        self.ui.threade5 = RunThread()
        self.ui.threade6 = RunThread()
        self.threadc1 = RunThread()
        self.ui.threadc2 = RunThread()
        self.ui.threadc3 = RunThread()
        self.ui.threadc4 = RunThread()
        self.ui.threadc5 = RunThread()
        self.ui.threadc6 = RunThread()
        self.ui.threadr1 = RunThread()
        self.threadg1 = RunThread()
        self.threadg3 = RunThread()
        self.threadg = RunThread()

        # 这里是“退出”按钮的信号槽：

        self.ui.pushButton_7.clicked.connect(QApplication.instance().quit)

        # 这里是每辆小车出错时候的警告弹窗：

        C3m = Car3message()
        self.ui.pushButton_26.clicked.connect(C3m.show)

        # 这里测试数据库：

        self.ui.pushButton_13.clicked.connect(OpenMySQL.open_mysql)
        self.ui.pushButton.clicked.connect(OpenSmartCars3D.Open)

        # 这里测试ZigBee串口通信：

        # self.ui.comboBox.activated[str].connect(order_list)

        # 这是“帮助”按钮的弹窗：

        h = HelpWindow()
        self.ui.pushButton_14.clicked.connect(h.show)

        # 这里定义每个小车单独弹窗：

        c1 = Car1()
        self.ui.pushButton_3.clicked.connect(c1.show)
        c2 = Car2()
        self.ui.pushButton_4.clicked.connect(c2.show)
        c3 = Car3()
        self.ui.pushButton_10.clicked.connect(c3.show)
        c4 = Car4()
        self.ui.pushButton_15.clicked.connect(c4.show)
        c5 = Car5()
        self.ui.pushButton_16.clicked.connect(c5.show)
        c6 = Car6()
        self.ui.pushButton_17.clicked.connect(c6.show)

        # 这是插入pyqtgraph的图像
        # self.ui.verticalLayout_3.addWidget(chart())

        # 这里测试和树莓派之间的通信：
        # self.ui.pushButton_6.clicked.connect(write)
        # self.ui.pushButton_6.clicked.connect(self.test)
        # self.ui.pushButton_24.clicked.connect(self.jump)
        # 这里是动作的信号：

        self.ui.comboBox.activated[str].connect(self.onActivated)
        self.ui.comboBox_2.activated[str].connect(self.onActivated)
        self.ui.comboBox_3.activated[str].connect(self.onActivated)
        self.ui.comboBox_4.activated[str].connect(self.onActivated)
        self.ui.comboBox_5.activated[str].connect(self.onActivated)
        self.ui.comboBox_6.activated[str].connect(self.onActivated)
        self.ui.comboBox_7.activated[str].connect(self.onActivated)
        self.ui.comboBox_8.activated[str].connect(self.onActivated)

        # 这里是每个小车的电量显示：

        self.ui.comboBox.activated[str].connect(self.showelectric)
        self.ui.comboBox_2.activated[str].connect(self.showelectric)
        self.ui.comboBox_3.activated[str].connect(self.showelectric)
        self.ui.comboBox_4.activated[str].connect(self.showelectric)
        self.ui.comboBox_5.activated[str].connect(self.showelectric)
        self.ui.comboBox_6.activated[str].connect(self.showelectric)
        self.ui.comboBox_7.activated[str].connect(self.showelectric)
        self.ui.comboBox_8.activated[str].connect(self.showelectric)

        # 这里定义进度栏：

        self.ui.comboBox.activated[str].connect(self.pbar_v)
        self.ui.comboBox_2.activated[str].connect(self.pbar_v)
        self.ui.comboBox_3.activated[str].connect(self.pbar_v)
        self.ui.comboBox_4.activated[str].connect(self.pbar_v)
        self.ui.comboBox_5.activated[str].connect(self.pbar_v)
        self.ui.comboBox_6.activated[str].connect(self.pbar_v)
        self.ui.comboBox_7.activated[str].connect(self.pbar_v)
        self.ui.comboBox_8.activated[str].connect(self.pbar_v)

        # 定义操控树莓派使小车开始启动：

        # self.ui.comboBox.activated[str].connect(self.startRPi)
        # self.ui.comboBox_2.activated[str].connect(self.startRPi)
        # self.ui.comboBox_3.activated[str].connect(self.startRPi)
        # self.ui.comboBox_4.activated[str].connect(self.startRPi)

        # 定义操控树莓派使小车制动：

        # self.ui.pushButton_18.clicked.connect(self.write2)
        # self.ui.pushButton_19.clicked.connect(self.write4)

        # 这里定义手动制动控制命令：
        
        self.ui.pushButton_18.clicked.connect(self.stopcar1)
        self.ui.pushButton_20.clicked.connect(self.stopcar3)
        # self.ui.pushButton_20.clicked.connect(self.ui.thread.anim.stop())
        # self.ui.pushButton_21.clicked.connect(self.ui.anim.stop())

        # 这里定义“演示编组”信号槽：
        self.ui.pushButton_6.clicked.connect(self.doAnimgroup)

        # 这里定义“翻越”信号槽：
        self.ui.pushButton_24.clicked.connect(self.climb)
        self.ui.pushButton_25.clicked.connect(self.fuck)
        self.i = 0

        # 这里是设置表格内容的信号：

        self.ui.comboBox.activated[str].connect(self.set_friction)
        self.ui.comboBox_2.activated[str].connect(self.set_sledge)
        self.ui.comboBox_3.activated[str].connect(self.set_outcomer)
        self.ui.comboBox_4.activated[str].connect(self.set_CCTV)
        self.ui.comboBox_5.activated[str].connect(self.set_friction)
        self.ui.comboBox_6.activated[str].connect(self.set_sledge)
        self.ui.comboBox_7.activated[str].connect(self.set_outcomer)
        self.ui.comboBox_8.activated[str].connect(self.set_CCTV)
        
        # 这里是定义小车弹窗：
        # self.ui.pushButton_3.clicked.connect(self.showcar1)

        # self.timer = QBasicTimer()
        self.step = 0

        # 这里是总览的信号：
        self.ui.comboBox.activated[str].connect(self.view_11)
        self.ui.comboBox_2.activated[str].connect(self.view_12)
        self.ui.comboBox_3.activated[str].connect(self.view_13)
        self.ui.comboBox_5.activated[str].connect(self.view_21)
        self.ui.comboBox_6.activated[str].connect(self.view_22)
        self.ui.comboBox_7.activated[str].connect(self.view_23)
        
        MainWindow.show()
        sys.exit(app.exec_())

    # 函数区

    def fuck(self):
        self.i += 1
        if self.i == 1:
            self.ui.label_60.setStyleSheet('background-color: rgb(213, 0, 0);')
            self.ui.label_95.setText('翻越')
        elif self.i == 2:
            self.ui.label_60.setStyleSheet('background-color: rgb(0, 213, 0);')
            self.ui.label_95.setText('正常')
        elif self.i == 3:
            self.ui.label_59.setStyleSheet('background-color: rgb(213, 0, 0);')
            self.ui.label_95.setText('编组')
            self.ui.label_77.setStyleSheet('background-color: rgb(213, 0, 0);')
            self.ui.label_97.setText('编组')
            self.doAnimgroup3()
            self.doAnimgroup1()
            self.write_group()

    def climb(self):
        self.startcar1()
        self.doAnim1()
    
    def jump(self):
        while True:
            if a == 1234: # 这里是判断来自树莓派的信号
                self.ui.label_60.setStyleSheet('background-color: rgb(213, 0, 0);')
                self.ui.label_95.setText('翻越')

    def test(self):
        while True:
            if a == 12314: # 同上
                self.ui.label_59.setStyleSheet('background-color: rgb(213, 0, 0);')
                self.ui.label_95.setText('编组')

    def OpenSmartCars3D(self):
        os.system("SmartCars3D.exe")
    
    def chart(self):
        hist_data = ts.get_hist_data('600519', start='2017-05-01', end='2017-11-24')
        data_list = []
        for dates,row in hist_data.iterrows():
            # 将时间转换为数字
            date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
            t = date2num(date_time)
            # t = dict(enumerate(datetime))
            open,high,close,low = row[:4]
            datas = (t,open,close,low,high)
            data_list.append(datas)
        axis_dict = dict(enumerate(axis))
        item = CandlestickItem(data_list)
        plt = pg.PlotWidget()
        plt.addItem(item,)
        plt.showGrid(x=True,y=True)
        return plt

    def timerEvent(self, e):
        timer1 = QBasicTimer()
        while self.step <=100:  
            # self.timer1.start(100, self)
            timer1.start(100, self.ui.progressBar_4)
            self.step = self.step + 1  
            self.ui.progressBar_4.setValue(self.step)

    # 这里是定义进度条：

    def pbar_v(self, text):
        if text == "1号车":
            self.time1()
        elif text == "2号车":
            self.time2()
        elif text == "3号车":
            self.time3()
        elif text == "4号车":
            self.time4()
        elif text == "5号车":
            self.time5()
        elif text == "6号车":
            self.time6()

    def time1(self):
        self.step1 = 0
        timer1 = QBasicTimer()
        while self.step1 <=100:
            # timer1.start(1, self.ui.progressBar)
            self.step1 = self.step1 + 0.001
            self.ui.progressBar.setValue(self.step1)

    def time2(self):
        self.step2 = 0
        timer2 = QBasicTimer()
        while self.step2 <=100:  
            # timer2.start(1, self.ui.progressBar_2)
            self.step2 = self.step2 + 0.001
            self.ui.progressBar_2.setValue(self.step2)

    def time3(self):
        self.step3 = 0
        timer3 = QBasicTimer()
        while self.step3 <=100:  
            # timer3.start(1, self.ui.progressBar_3)
            self.step3 = self.step3 + 0.001  
            self.ui.progressBar_3.setValue(self.step3)

    def time4(self):
        self.step4 = 0
        timer4 = QBasicTimer()
        while self.step4 <=100:  
            # timer4.start(1, self.ui.progressBar_4)
            self.step4 = self.step4 + 0.0005 
            self.ui.progressBar_4.setValue(self.step4)

    def time5(self):
        self.step5 = 0
        timer5 = QBasicTimer()
        while self.step5 <=100:  
            # timer5.start(1, self.ui.progressBar_5)
            self.step5 = self.step5 + 0.001 
            self.ui.progressBar_5.setValue(self.step5)   

    def time6(self):
        self.step6 = 0
        timer6 = QBasicTimer()
        while self.step6 <=100:  
            # timer6.start(1, self.ui.progressBar_6)
            self.step6 = self.step6 + 0.001
            self.ui.progressBar_6.setValue(self.step6)

    # 这里定义手动制动按钮，一个函数用于向树莓派发送数据，一个函数用于停止动画的演示

    def stopcar1(self):
        a = 'FE 05 91 91 1F 00 02 FF'
        a_list = []
        for i in a.split():
            a_list.append(binascii.a2b_hex(i))
    
        ser.writelines(a_list)

    def stopcar3(self):
        a = 'FE 05 91 91 2F 00 02 FF'
        a_list = []
        for i in a.split():
            a_list.append(binascii.a2b_hex(i))
    
        ser.writelines(a_list)

    # 这里定义“演示编组”：

    def doAnimgroup(self):
        self.ui.label_59.setStyleSheet('background-color: rgb(213, 0, 0);')
        self.ui.label_95.setText('编组')
        self.ui.label_77.setStyleSheet('background-color: rgb(213, 0, 0);')
        self.ui.label_97.setText('编组')
        self.doAnimgroup3()
        self.doAnimgroup1()
        self.write_group()

    def write_group(self):
        a = 'FE 05 91 91 1F 00 03 FF'
        a_list = []
        for i in a.split():
            a_list.append(binascii.a2b_hex(i))
        ser.writelines(a_list)

    def doAnimgroup3(self):
        self.threadg3.anim = QPropertyAnimation(self.ui.frame_3, b"geometry")
        self.threadg3.anim.setDuration(6000)
        self.threadg3.anim.setStartValue(QRect(830, 100, 41, 101))
        self.threadg3.anim.setEndValue(QRect(1230, 100, 41,101))
        self.threadg3.anim.start()

    def doAnimgroup1(self):
        self.threadg1.anim = QPropertyAnimation(self.ui.frame, b"geometry")
        self.threadg1.anim.setDuration(6000)
        self.threadg1.anim.setStartValue(QRect(790, 100, 41, 101))
        self.threadg1.anim.setEndValue(QRect(1190, 100, 41,101))
        self.threadg1.anim.start()

    # 这里是定义启动小车的函数，向树莓派发送串口数据的同时也启动软件的动画演示：
    
    def onActivated(self, text):
        if text == "4号车":
            self.doAnim4()
        elif text == "5号车":
            self.doAnim4()
        elif text == "6号车":
            self.doAnim6()
        elif text == "1号车":
            # 第一条命令用于和1号车通信
            # self.startcar1()
            self.doAnim1()
        elif text == "2号车":
            self.doAnim5()
        elif text == "3号车":
            # 第一条命令用于和3号车通信
            # self.startcar3()
            self.doAnim3()

    def startcar1(self):
        a = 'FE 05 91 91 1F 00 01 FF'
        a_list = []
        for i in a.split():
            a_list.append(binascii.a2b_hex(i))
    
        ser.writelines(a_list)   

    def startcar3(self):
        a = 'FE 05 91 91 2F 00 01 FF'
        a_list = []
        for i in a.split():
            a_list.append(binascii.a2b_hex(i))
    
        ser.writelines(a_list)   

    def doAnim1(self):
        self.anim = QPropertyAnimation(self.ui.frame, b"geometry")
        self.anim.setDuration(20000)
        self.anim.setStartValue(QRect(150, 100, 41, 101))
        self.anim.setKeyValueAt(0.40, QRect(450, 100, 41, 101))
        self.anim.setKeyValueAt(0.50, QRect(470, 50, 41, 101))
        self.anim.setKeyValueAt(0.60, QRect(490, 100, 41, 101))
        self.anim.setEndValue(QRect(790, 100, 41,101))
        self.anim.start()

    def doAnimLabel1(self):
        self.threadc1.anim = QPropertyAnimation(self.ui.label_60, b"color")
        self.threadc1.anim.setDuration(10000)
        self.threadc1.anim.setStartValue(QColor(0, 213, 0))
        self.threadc1.anim.setKeyValueAt(0.40, QColor(0, 213, 0))
        self.threadc1.anim.setKeyValueAt(0.50, QColor(213, 0, 0))
        self.threadc1.anim.setKeyValueAt(0.60, QColor(0, 213, 0))
        self.threadc1.anim.setEndValue(QColor(0, 213, 0))
        self.threadc1.anim.start()

    def doAnim2(self):
        self.ui.anim = QPropertyAnimation(self.ui.frame_2, b"geometry")
        self.ui.anim.setDuration(60000)
        self.ui.anim.setStartValue(QRect(270, 100, 41, 101)) 
        self.ui.anim.setEndValue(QRect(1270, 100, 41,101))
        self.ui.anim.start()

    def doAnim3(self):
        self.thread.anim = QPropertyAnimation(self.ui.frame_3, b"geometry")
        self.thread.anim.setDuration(10000)
        self.thread.anim.setStartValue(QRect(540, 100, 41, 101))
        self.thread.anim.setEndValue(QRect(830, 100, 41,101))
        self.thread.anim.start()

    def doAnim4(self):
        self.thread2.anim = QPropertyAnimation(self.ui.frame_4, b"geometry")
        self.thread2.anim.setDuration(60000)
        self.thread2.anim.setStartValue(QRect(135, 345, 41, 101))
        self.thread2.anim.setEndValue(QRect(1270, 345, 41,101))
        self.thread2.anim.start()

    def doAnim5(self):
        self.thread3.anim = QPropertyAnimation(self.ui.frame_5, b"geometry")
        self.thread3.anim.setDuration(60000)
        self.thread3.anim.setStartValue(QRect(135, 345, 41, 101))
        self.thread3.anim.setEndValue(QRect(1270, 345, 41,101))
        self.thread3.anim.start()

    def doAnim6(self):
        self.thread3_1.anim = QPropertyAnimation(self.ui.frame_6, b"geometry")
        self.thread3_1.anim.setDuration(60000)
        self.thread3_1.anim.setStartValue(QRect(135, 345, 41, 101))
        self.thread3_1.anim.setEndValue(QRect(1270, 345, 41,101))
        self.thread3_1.anim.start()

    # 这里是定义显示每辆小车实时电量的函数组：

    def showelectric(self, text):
        if text == "1号车":
            self.doAnim_electric1()
        elif text == "2号车":
            self.doAnim_electric2()
        elif text == "3号车":
            self.doAnim_electric3()
        elif text == "4号车":
            self.doAnim_electric4()
        elif text == "5号车":
            self.doAnim_electric5()
        elif text == "6号车":
            self.doAnim_electric6()

    def doAnim_electric1(self):
        self.ui.threade1.anim = QPropertyAnimation(self.ui.label_33, b"geometry")
        self.ui.threade1.anim.setDuration(30000)
        self.ui.threade1.anim.setStartValue(QRect(0, 10, 40, 5))
        self.ui.threade1.anim.setEndValue(QRect(0, 10, 20, 5))
        self.ui.threade1.anim.start()

    def doAnim_electric2(self):
        self.ui.threade2.anim = QPropertyAnimation(self.ui.label_34, b"geometry")
        self.ui.threade2.anim.setDuration(30000)
        self.ui.threade2.anim.setStartValue(QRect(0, 10, 40, 5)) 
        self.ui.threade2.anim.setEndValue(QRect(0, 10, 20, 5))
        self.ui.threade2.anim.start()

    def doAnim_electric3(self):
        self.ui.threade3.anim = QPropertyAnimation(self.ui.label_35, b"geometry")
        self.ui.threade3.anim.setDuration(30000)
        self.ui.threade3.anim.setStartValue(QRect(0, 10, 40, 5))
        self.ui.threade3.anim.setEndValue(QRect(0, 10, 20, 5))
        self.ui.threade3.anim.start()

    def doAnim_electric4(self):
        self.ui.threade4.anim = QPropertyAnimation(self.ui.label_36, b"geometry")
        self.ui.threade4.anim.setDuration(30000)
        self.ui.threade4.anim.setStartValue(QRect(0, 10, 40, 5))
        self.ui.threade4.anim.setEndValue(QRect(0, 10, 20, 5))
        self.ui.threade4.anim.start()

    def doAnim_electric5(self):
        self.ui.threade5.anim = QPropertyAnimation(self.ui.label_37, b"geometry")
        self.ui.threade5.anim.setDuration(30000)
        self.ui.threade5.anim.setStartValue(QRect(0, 10, 40, 5))
        self.ui.threade5.anim.setEndValue(QRect(0, 10, 20, 5))
        self.ui.threade5.anim.start()

    def doAnim_electric6(self):
        self.ui.threade6.anim = QPropertyAnimation(self.ui.label_85, b"geometry")
        self.ui.threade6.anim.setDuration(30000)
        self.ui.threade6.anim.setStartValue(QRect(0, 10, 40, 5))
        self.ui.threade6.anim.setEndValue(QRect(0, 10, 20, 5))
        self.ui.threade6.anim.start()

    # 这里是让表格显示小车的工作状态的函数组：

    def set_friction(self,text):
        if text == "1号车":
            self.setf1()
        elif text == "2号车":
            self.setf2()
        elif text == "3号车":
            self.setf3()
        elif text == "4号车":
            self.setf4()
        elif text == "5号车":
            self.setf5()
        elif text == "6号车":
            self.setf6()

    def setf1(self):
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("检测项目1"))

    def setf2(self):
        self.ui.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(1,1, QtWidgets.QTableWidgetItem("检测项目1"))

    def setf3(self):
        self.ui.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("检测项目1"))

    def setf4(self):
        self.ui.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(3,1, QtWidgets.QTableWidgetItem("检测项目1"))

    def setf5(self):
        self.ui.tableWidget.setItem(4,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(4,1, QtWidgets.QTableWidgetItem("检测项目1"))

    def setf6(self):
        self.ui.tableWidget.setItem(5,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(5,1, QtWidgets.QTableWidgetItem("检测项目1"))

    def set_sledge(self,text):
        if text == "1号车":
            self.sets1()
        elif text == "2号车":
            self.sets2()
        elif text == "3号车":
            self.sets3()
        elif text == "4号车":
            self.sets4()
        elif text == "5号车":
            self.sets5()
        elif text == "6号车":
            self.sets6()

    def sets1(self):
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("检测项目2"))

    def sets2(self):
        self.ui.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(1,1, QtWidgets.QTableWidgetItem("检测项目2"))

    def sets3(self):
        self.ui.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("检测项目2"))

    def sets4(self):
        self.ui.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(3,1, QtWidgets.QTableWidgetItem("检测项目2"))

    def sets5(self):
        self.ui.tableWidget.setItem(4,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(4,1, QtWidgets.QTableWidgetItem("检测项目2"))

    def sets6(self):
        self.ui.tableWidget.setItem(5,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(5,1, QtWidgets.QTableWidgetItem("检测项目2"))

    def set_outcomer(self,text):
        if text == "1号车":
            self.seto1()
        elif text == "2号车":
            self.seto2()
        elif text == "3号车":
            self.seto3()
        elif text == "4号车":
            self.seto4()
        elif text == "5号车":
            self.seto5()
        elif text == "6号车":
            self.seto6()

    def seto1(self):
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("检测项目3"))

    def seto2(self):
        self.ui.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(1,1, QtWidgets.QTableWidgetItem("检测项目3"))

    def seto3(self):
        self.ui.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("检测项目3"))

    def seto4(self):
        self.ui.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(3,1, QtWidgets.QTableWidgetItem("检测项目3"))

    def seto5(self):
        self.ui.tableWidget.setItem(4,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(4,1, QtWidgets.QTableWidgetItem("检测项目3"))

    def seto6(self):
        self.ui.tableWidget.setItem(5,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(5,1, QtWidgets.QTableWidgetItem("检测项目3"))

    def set_CCTV(self,text):
        if text == "1号车":
            self.setc1()
        elif text == "2号车":
            self.setc2()
        elif text == "3号车":
            self.setc3()
        elif text == "4号车":
            self.setc4()
        elif text == "5号车":
            self.setc5()
        elif text == "6号车":
            self.setc6()

    def setc1(self):
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("视频监控"))

    def setc2(self):
        self.ui.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(1,1, QtWidgets.QTableWidgetItem("视频监控"))

    def setc3(self):
        self.ui.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("视频监控"))

    def setc4(self):
        self.ui.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(3,1, QtWidgets.QTableWidgetItem("视频监控"))

    def setc5(self):
        self.ui.tableWidget.setItem(4,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(4,1, QtWidgets.QTableWidgetItem("视频监控"))

    def setc6(self):
        self.ui.tableWidget.setItem(5,0, QtWidgets.QTableWidgetItem("正常巡检"))
        self.ui.tableWidget.setItem(5,1, QtWidgets.QTableWidgetItem("视频监控"))

    # 定义上行线磨损状态移动的命令：
    def view_11(self):
        self.ui.thread4.anim = QPropertyAnimation(self.ui.label, b"geometry")
        self.ui.thread4.anim.setDuration(60000)
        self.ui.thread4.anim.setStartValue(QRect(120, 60, 31, 21))
        self.ui.thread4.anim.setEndValue(QRect(120, 60, 451, 21))
        self.ui.thread4.anim.start()

    # 定义上行线裂纹状态移动的命令：
    def view_12(self):
        self.ui.thread5.anim = QPropertyAnimation(self.ui.label_67, b"geometry")
        self.ui.thread5.anim.setDuration(60000)
        self.ui.thread5.anim.setStartValue(QRect(120, 90, 31, 21))
        self.ui.thread5.anim.setEndValue(QRect(120, 90, 451, 21))
        self.ui.thread5.anim.start()

    # 定义上行线异物状态移动的命令：
    def view_13(self):
        self.ui.thread6.anim = QPropertyAnimation(self.ui.label_68, b"geometry")
        self.ui.thread6.anim.setDuration(60000)
        self.ui.thread6.anim.setStartValue(QRect(120, 120, 31, 21))
        self.ui.thread6.anim.setEndValue(QRect(120, 120, 451, 21))
        self.ui.thread6.anim.start()

    # 定义下行线磨损状态移动的命令：
    def view_21(self):
        self.ui.thread7.anim = QPropertyAnimation(self.ui.label_2, b"geometry")
        self.ui.thread7.anim.setDuration(60000)
        self.ui.thread7.anim.setStartValue(QRect(120, 180, 31, 21))
        self.ui.thread7.anim.setEndValue(QRect(120, 180, 451, 21))
        self.ui.thread7.anim.start()

    # 定义下行线裂纹状态移动的命令：
    def view_22(self):
        self.ui.thread8.anim = QPropertyAnimation(self.ui.label_69, b"geometry")
        self.ui.thread8.anim.setDuration(60000)
        self.ui.thread8.anim.setStartValue(QRect(120, 210, 31, 21))
        self.ui.thread8.anim.setEndValue(QRect(120, 210, 451, 21))
        self.ui.thread8.anim.start()

    # 定义下行线异物状态移动的命令：
    def view_23(self):
        self.ui.thread9.anim = QPropertyAnimation(self.ui.label_70, b"geometry")
        self.ui.thread9.anim.setDuration(60000)
        self.ui.thread9.anim.setStartValue(QRect(120, 240, 31, 21))
        self.ui.thread9.anim.setEndValue(QRect(120, 240, 451, 21))
        self.ui.thread9.anim.start()


if __name__ == "__main__":
    MainWindow()
