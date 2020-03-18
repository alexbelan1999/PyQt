from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Progress_recognition1(object):
    def setupUi(self, Progress_recognition1):
        Progress_recognition1.setObjectName("Progress_recognition1")
        Progress_recognition1.setFixedSize(450, 330)
        ico = QtGui.QIcon("mylogo.png")
        Progress_recognition1.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Progress_recognition1)
        self.centralwidget.setObjectName("centralwidget")

        self.label_progress = QtWidgets.QLabel(self.centralwidget)
        self.label_progress.setGeometry(QtCore.QRect(100, 20, 170, 25))
        self.label_progress.setFont(font)
        self.label_progress.setObjectName("label_progress")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(100, 50, 250, 30))
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 90, 250, 25))
        self.progressBar.setFont(font)
        self.progressBar.setObjectName("progressBar")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 130, 250, 100))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.pushButton_report = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_report.setGeometry(QtCore.QRect(100, 240, 250, 30))
        self.pushButton_report.setFont(font)
        self.pushButton_report.setObjectName("pushButton_report")

        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setGeometry(QtCore.QRect(100, 280, 140, 30))
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(260, 280, 90, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Progress_recognition1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Progress_recognition1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Progress_recognition1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Progress_recognition1)
        self.statusbar.setObjectName("statusbar")
        Progress_recognition1.setStatusBar(self.statusbar)

        self.retranslateUi(Progress_recognition1)
        QtCore.QMetaObject.connectSlotsByName(Progress_recognition1)

    def retranslateUi(self, Progress_recognition1):
        _translate = QtCore.QCoreApplication.translate
        Progress_recognition1.setWindowTitle(_translate("Progress_recognition1", "Progress_recognition1"))
        self.label_progress.setText(_translate("Progress_recognition1", "Обработка видео"))
        self.pushButton_menu.setText(_translate("Progress_recognition1", "В главное меню"))
        self.pushButton_exit.setText(_translate("Progress_recognition1", "Выход"))
        self.pushButton_start.setText(_translate("Progress_recognition1", "Начало распознавания"))
        self.pushButton_report.setText(_translate("Progress_recognition1", "Отправить отчет"))
