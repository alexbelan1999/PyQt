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

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 180, 30))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 180, 20))
        self.lineEdit.setFont(font)
        self.lineEdit.setDisabled(True)
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 180, 20))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 180, 20))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 160, 180, 20))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 195, 180, 20))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 240, 180, 20))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 280, 180, 20))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")

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
        self.label.setText(_translate("Info", "Базу данных:"))
        self.label_2.setText(_translate("Info", "Пользователь:"))
        self.label_3.setText(_translate("Info", "Пароль:"))
        self.label_4.setText(_translate("Info", "Host:"))
