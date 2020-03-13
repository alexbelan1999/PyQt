from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.setFixedSize(520, 420)
        ico = QtGui.QIcon("mylogo.png")
        Info.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Info)
        self.centralwidget.setObjectName("centralwidget")

        self.label_db = QtWidgets.QLabel(self.centralwidget)
        self.label_db.setGeometry(QtCore.QRect(170, 10, 180, 30))
        self.label_db.setFont(font)
        self.label_db.setObjectName("label_db")

        self.lineEdit_db = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_db.setGeometry(QtCore.QRect(170, 50, 180, 20))
        self.lineEdit_db.setFont(font)
        self.lineEdit_db.setDisabled(True)
        self.lineEdit_db.setObjectName("lineEdit_db")

        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(170, 90, 180, 20))
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")

        self.lineEdit_user = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_user.setGeometry(QtCore.QRect(170, 120, 180, 20))
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setDisabled(True)
        self.lineEdit_user.setObjectName("lineEdit_user")

        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(170, 160, 180, 20))
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")

        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(170, 195, 180, 20))
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setDisabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.label_host = QtWidgets.QLabel(self.centralwidget)
        self.label_host.setGeometry(QtCore.QRect(170, 240, 180, 20))
        self.label_host.setFont(font)
        self.label_host.setObjectName("label_host")

        self.lineEdit_host = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_host.setGeometry(QtCore.QRect(170, 280, 180, 20))
        self.lineEdit_host.setFont(font)
        self.lineEdit_host.setDisabled(True)
        self.lineEdit_host.setObjectName("lineEdit_host")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(170, 320, 90, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(260, 320, 90, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")

        Info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Info)
        self.statusbar.setObjectName("statusbar")
        Info.setStatusBar(self.statusbar)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Info"))
        self.label_db.setText(_translate("Info", "Базу данных:"))
        self.label_user.setText(_translate("Info", "Пользователь:"))
        self.label_password.setText(_translate("Info", "Пароль:"))
        self.label_host.setText(_translate("Info", "Host:"))
        self.pushButton_back.setText(_translate("Info", "Назад"))
        self.pushButton_exit.setText(_translate("Info", "Выход"))
