from PyQt5 import QtCore, QtGui, QtWidgets
import postgresql as pg

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 180, 30))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 180, 20))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 180, 20))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 180, 20))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 160, 180, 20))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 195, 180, 20))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 240, 180, 20))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 280, 180, 20))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 320, 90, 30))
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.btnClicked)
        self.pushButton.setObjectName("pushButton")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 360, 90, 30))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 320, 90, 30))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")

        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Введите базу данных:"))
        self.label_2.setText(_translate("Login", "Пользователь:"))
        self.label_3.setText(_translate("Login", "Пароль:"))
        self.label_4.setText(_translate("Login", "Host:"))
        self.pushButton.setText(_translate("Login", "Test"))
        self.pushButton_2.setText(_translate("Login", "Login"))

    def btnClicked(self):
        dbname = self.lineEdit.text()
        user = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        host = self.lineEdit_4.text()
        print(dbname)
        print(user)
        print(password)
        print(host)
        check = pg.check_connection(dbname,user,password,host)

        if check:
            self.label_5.setText("OK!")
        else:
            self.label_5.setText("ERROR!")