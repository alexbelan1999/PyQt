from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DB(object):
    def setupUi(self, DB):
        DB.setObjectName("Camera")
        DB.setFixedSize(600, 500)
        ico = QtGui.QIcon("mylogo.png")
        DB.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(DB)
        self.centralwidget.setObjectName("centralwidget")
        self.label_table = QtWidgets.QLabel(self.centralwidget)
        self.label_table.setGeometry(QtCore.QRect(50, 20, 130, 30))
        self.label_table.setFont(font)
        self.label_table.setObjectName("label_table")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 60, 500, 330))
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 420, 140, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(240, 420, 170, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        DB.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DB)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        DB.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DB)
        self.statusbar.setObjectName("statusbar")
        DB.setStatusBar(self.statusbar)

        self.retranslateUi(DB)
        QtCore.QMetaObject.connectSlotsByName(DB)

    def retranslateUi(self, DB):
        _translate = QtCore.QCoreApplication.translate
        DB.setWindowTitle(_translate("DB", "DB"))
        self.label_table.setText(_translate("DB", "Таблица"))
        self.pushButton_back.setText(_translate("DB", "Назад"))
        self.pushButton_exit.setText(_translate("DB", "Выход"))
