import datetime
import glob
import os
import sys
import time

import postgresql as pg
from PyQt5 import QtWidgets

import test2
from progressrec1 import Ui_Progress_recognition1


class Progress_recognition1(QtWidgets.QMainWindow):
    video = ""
    dir = ""
    progress_recognition1_info = []

    def __init__(self, info=["", "", "", ""], file = "", video = ""):
        super(Progress_recognition1, self).__init__()
        self.ui = Ui_Progress_recognition1()
        self.ui.setupUi(self)
        Progress_recognition1.progress_recognition1_info = info
        Progress_recognition1.file = file
        Progress_recognition1.video = video
        self.ui.progressBar.setValue(0)
        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_start.clicked.connect(self.start_progress)
        self.ui.pushButton_report.clicked.connect(self.report)

    def back_menu(self):
        self.open_menu = test2.Menu(Progress_recognition1.progress_recognition1_info)
        print(Progress_recognition1.progress_recognition1_info)
        self.open_menu.show()
        self.close()

    def start_progress(self):
        self.ui.pushButton_exit.setDisabled(True)
        self.ui.pushButton_menu.setDisabled(True)
        self.ui.pushButton_report.setDisabled(True)
        self.progress()

    def progress(self):
        path = Progress_recognition1.dir + "/*"
        print(path)
        files = len(glob.glob(path))
        number = 1
        for file in glob.glob(path):
            time.sleep(2)
            self.ui.textEdit.append(file)
            self.ui.progressBar.setValue(round(number/files,2) * 100)
            number += 1
            if  number == files:
                self.ui.pushButton_exit.setDisabled(False)
                self.ui.pushButton_menu.setDisabled(False)
                self.ui.pushButton_report.setDisabled(False)

    def report(self):
        report = self.ui.textEdit.toPlainText()
        report = list(report.split('\n'))
        print(report)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        persons = []
        persons.append(["Alex", timestamp])
        print(pg.insert(persons))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Progress_recognition1()
    application.show()

    sys.exit(app.exec())
