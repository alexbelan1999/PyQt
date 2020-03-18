from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rec1(object):
    def setupUi(self, Rec1):
        Rec1.setObjectName("Rec1")
        Rec1.setFixedSize(450, 200)
        ico = QtGui.QIcon("mylogo.png")
        Rec1.setWindowIcon(ico)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        
        self.centralwidget = QtWidgets.QWidget(Rec1)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton_photo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_photo.setGeometry(QtCore.QRect(50, 20, 350, 30))
        self.pushButton_photo.setFont(font)
        self.pushButton_photo.setObjectName("pushButton_photo")
        
        self.pushButton_video = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_video.setGeometry(QtCore.QRect(50, 60, 350, 30))
        self.pushButton_video.setFont(font)
        self.pushButton_video.setObjectName("pushButton_video")
        
        self.pushButton_camera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_camera.setGeometry(QtCore.QRect(50, 100, 350, 30))
        self.pushButton_camera.setFont(font)
        self.pushButton_camera.setObjectName("pushButton_camera")
        
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 140, 170, 30))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(230, 140, 170, 30))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        Rec1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Rec1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Rec1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Rec1)
        self.statusbar.setObjectName("statusbar")
        Rec1.setStatusBar(self.statusbar)

        self.retranslateUi(Rec1)
        QtCore.QMetaObject.connectSlotsByName(Rec1)

    def retranslateUi(self, Rec1):
        _translate = QtCore.QCoreApplication.translate
        Rec1.setWindowTitle(_translate("Rec1", "Recognition"))
        self.pushButton_photo.setText(_translate("Rec1", "Распознавание по фото"))
        self.pushButton_video.setText(_translate("Rec1", "Распознавие по видео"))
        self.pushButton_camera.setText(_translate("Rec1", "Распознавание с помощью веб-камеры"))
        self.pushButton_back.setText(_translate("Rec1", "Назад"))
        self.pushButton_exit.setText(_translate("Rec1", "Выход"))
