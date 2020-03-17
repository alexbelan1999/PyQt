import glob
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import test5
from rec2 import Ui_Rec2


class Rec2(QtWidgets.QMainWindow):
    file = ""
    dir = ""
    rec2_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Rec2, self).__init__()
        self.ui = Ui_Rec2()
        self.ui.setupUi(self)
        Rec2.rec2_info = info
        path = os.getcwd() + "/*"
        files = len(glob.glob(path))
        for file in glob.glob(path):
            self.ui.comboBox.addItem(file)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_next.clicked.connect(self.next)
        self.ui.pushButton_dir.clicked.connect(self.open_dir)

    def back(self):
        self.open_rec1 = test5.Rec1(Rec2.rec2_info)
        self.open_rec1.show()
        self.close()

    def next(self):
        Rec2.file = self.ui.comboBox.currentText()
        Rec2.dir = self.ui.lineEdit_dir.text()
        print(Rec2.file," ", Rec2.dir)
        # self.open_rec3 = test7.Rec3(Rec2.rec2_info,Rec2.file,Rec2.dir)
        # self.open_rec3.show()
        self.close()

    def open_dir(self):
        fdir = QFileDialog.getExistingDirectory(self, 'Open dir', os.getcwd())
        self.ui.lineEdit_dir.setText(fdir)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Rec2()
    application.show()

    sys.exit(app.exec())
