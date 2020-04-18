import glob
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import test5
import test9
from rec3 import Ui_Rec3


class Rec3(QtWidgets.QMainWindow):
    file = ""
    video = ""
    rec3_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Rec3, self).__init__()
        self.ui = Ui_Rec3()
        self.ui.setupUi(self)
        Rec3.rec3_info = info
        path = os.getcwd() + "/*"
        files = len(glob.glob(path))
        for file in glob.glob(path):
            self.ui.comboBox.addItem(file)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_next.clicked.connect(self.next)
        self.ui.pushButton_file.clicked.connect(self.open_file)

    def back(self):
        self.open_rec1 = test5.Rec1(Rec3.rec3_info)
        self.open_rec1.show()
        self.close()

    def next(self):
        Rec3.file = self.ui.comboBox.currentText()
        Rec3.video = self.ui.lineEdit_file.text()
        self.open_progressrec1 = test9.Progress_recognition1(Rec3.rec3_info, Rec3.file, Rec3.video)
        self.open_progressrec1.show()
        self.close()

    def open_file(self):
        video = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"*mp4")[0]
        self.ui.lineEdit_file.setText(video)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Rec3()
    application.show()

    sys.exit(app.exec())
