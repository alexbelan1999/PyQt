from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Hello(object):
    def setupUi(self, Hello):
        Hello.setObjectName("Hello")
        Hello.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Hello)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Hello.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hello)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        Hello.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hello)
        self.statusbar.setObjectName("statusbar")
        Hello.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menutest.menuAction())

        self.retranslateUi(Hello)
        QtCore.QMetaObject.connectSlotsByName(Hello)

    def retranslateUi(self, Hello):
        _translate = QtCore.QCoreApplication.translate
        Hello.setWindowTitle(_translate("Hello", "Hello"))
        self.label.setText(_translate("Hello", "Привет"))
        self.menutest.setTitle(_translate("Hello", "test"))
