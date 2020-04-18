import datetime
import glob
import sys
import time

from PyQt5 import QtWidgets

import test2
import test11
from progressrec import Ui_Progress_recognition


class Progress_recognition(QtWidgets.QMainWindow):
    file = ""
    dir = ""
    progress_recognition_info = []

    def __init__(self, info=["", "", "", ""], file="", dir=""):
        super(Progress_recognition, self).__init__()
        self.ui = Ui_Progress_recognition()
        self.ui.setupUi(self)
        Progress_recognition.progress_recognition_info = info
        Progress_recognition.file = file
        Progress_recognition.dir = dir
        self.ui.progressBar.setValue(0)
        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_start.clicked.connect(self.start_progress)
        self.ui.pushButton_report.clicked.connect(self.report)

    def back_menu(self):
        self.open_menu = test2.Menu(Progress_recognition.progress_recognition_info)
        self.open_menu.show()
        self.close()

    def start_progress(self):
        self.ui.pushButton_exit.setDisabled(True)
        self.ui.pushButton_menu.setDisabled(True)
        self.ui.pushButton_report.setDisabled(True)
        self.progress()

    def progress(self):
        path = Progress_recognition.dir + "/*"
        print(path)
        files = len(glob.glob(path))
        number = 1
        for file in glob.glob(path):
            time.sleep(2)
            self.ui.textEdit.append(file)
            self.ui.progressBar.setValue(round(number / files, 2) * 100)
            number += 1
            if number == files:
                self.ui.pushButton_exit.setDisabled(False)
                self.ui.pushButton_menu.setDisabled(False)
                self.ui.pushButton_report.setDisabled(False)

    def report(self):
        report = self.ui.textEdit.toPlainText()
        report = list(report.split('\n'))
        print(report)
        person = ["Alex","Dima","Vitaly","Ivan","Petr","Artem","Andrey","Alex","Dima","Vitaly","Ivan","Petr","Artem","Andrey","Alex","Dima","Vitaly","Ivan","Petr","Artem","Andrey","Alex","Dima","Vitaly","Ivan","Petr","Artem","Andrey"]
        self.open_report = test11.Report(Progress_recognition.progress_recognition_info,person)
        self.open_report.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Progress_recognition()
    application.show()

    sys.exit(app.exec())
