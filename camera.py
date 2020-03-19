
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Camera(object):
    def setupUi(self, Camera):
        Camera.setObjectName("Camera")
        Camera.setFixedSize(950, 700)
        ico = QtGui.QIcon("mylogo.png")
        Camera.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        
        self.centralwidget = QtWidgets.QWidget(Camera)

        self.label_combo = QtWidgets.QLabel(self.centralwidget)
        self.label_combo.setGeometry(QtCore.QRect(50, 20, 450, 25))
        self.label_combo.setFont(font)
        self.label_combo.setObjectName("label_combo")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 60, 450, 25))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 100, 130, 25))
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_video = QtWidgets.QLabel(self.centralwidget)
        self.label_video.setGeometry(QtCore.QRect(50, 140, 640, 480))
        self.label_video.setObjectName("label_video")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(700, 140, 200, 482))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(50, 650, 130, 30))
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(190, 650, 130, 30))
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")

        self.pushButton_report = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_report.setGeometry(QtCore.QRect(330, 650, 150, 30))
        self.pushButton_report.setFont(font)
        self.pushButton_report.setObjectName("pushButton_report")

        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setGeometry(QtCore.QRect(490, 650, 150, 30))
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(650, 650, 130, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Camera.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Camera)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Camera.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Camera)
        self.statusbar.setObjectName("statusbar")
        Camera.setStatusBar(self.statusbar)

        self.retranslateUi(Camera)
        QtCore.QMetaObject.connectSlotsByName(Camera)

    def retranslateUi(self, Camera):
        _translate = QtCore.QCoreApplication.translate
        Camera.setWindowTitle(_translate("Camera", "Camera"))
        self.label.setText(_translate("Camera", "Видео"))
        self.label_video.setText(_translate("Camera", ""))
        self.pushButton_start.setText(_translate("Camera", "Старт"))
        self.pushButton_stop.setText(_translate("Camera", "Стоп"))
        self.pushButton_menu.setText(_translate("Camera", "В главное меню"))
        self.pushButton_exit.setText(_translate("Camera", "Выход"))
        self.pushButton_report.setText(_translate("Camera", "Отправить отчет"))
        self.label_combo.setText(_translate("Camera", "Выберете подготовленный файл для распознавания"))
