from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rec3(object):
    def setupUi(self, Rec3):
        Rec3.setObjectName("Rec3")
        Rec3.setFixedSize(520, 270)
        ico = QtGui.QIcon("mylogo.png")
        Rec3.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.centralwidget = QtWidgets.QWidget(Rec3)
        self.centralwidget.setObjectName("centralwidget")

        self.label_combo = QtWidgets.QLabel(self.centralwidget)
        self.label_combo.setGeometry(QtCore.QRect(50, 20, 420, 30))
        self.label_combo.setFont(font)
        self.label_combo.setObjectName("label_combo")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 60, 420, 30))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setGeometry(QtCore.QRect(50, 100, 420, 30))
        self.pushButton_file.setFont(font)
        self.pushButton_file.setObjectName("pushButton_file")

        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(50, 140, 420, 30))
        self.label_file.setFont(font)
        self.label_file.setObjectName("label_file")

        self.lineEdit_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file.setGeometry(QtCore.QRect(50, 180, 420, 30))
        self.lineEdit_file.setFont(font)
        self.lineEdit_file.setObjectName("lineEdit_file")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 220, 130, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(190, 220, 130, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(330, 220, 130, 30))
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")

        Rec3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Rec3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Rec3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Rec3)
        self.statusbar.setObjectName("statusbar")
        Rec3.setStatusBar(self.statusbar)

        self.retranslateUi(Rec3)
        QtCore.QMetaObject.connectSlotsByName(Rec3)

    def retranslateUi(self, Rec3):
        _translate = QtCore.QCoreApplication.translate
        Rec3.setWindowTitle(_translate("Rec3", "Recognition"))
        self.label_combo.setText(_translate("Rec3", "Выберете подготовленный файл для распознавания"))
        self.pushButton_file.setText(_translate("Rec3", "Выберите видео файл для распознавания"))
        self.label_file.setText(_translate("Rec3", "Файл:"))
        self.pushButton_back.setText(_translate("Rec3", "Назад"))
        self.pushButton_exit.setText(_translate("Rec3", "Выход"))
        self.pushButton_next.setText(_translate("Rec3", "Далее"))
