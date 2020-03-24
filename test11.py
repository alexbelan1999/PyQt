import datetime
import glob
import sys
import time

from PyQt5 import QtWidgets

import postgresql as pg
import test2
from report import Ui_Report


class Report(QtWidgets.QMainWindow):
    report = []
    report_info = []

    def __init__(self, info=["", "", "", ""], report = []):
        super(Report, self).__init__()
        self.ui = Ui_Report()
        self.ui.setupUi(self)
        Report.report_info = info
        Report.report = report
        self.ui.label_instructor2.setText(info[1])
        for person in report:
            self.ui.textEdit.append(person)
        self.ui.textEdit.setReadOnly(True)
        date2 = datetime.datetime.now().strftime("%d-%m-%Y")
        time2 = datetime.datetime.now().strftime("%H:%M:%S")
        self.ui.label_time2.setText(time2)
        self.ui.label_date2.setText(date2)
        self.ui.pushButton_back.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_send.clicked.connect(self.send)

    def back_menu(self):
        self.open_menu = test2.Menu(Report.progress_recognition_info)
        self.open_menu.show()
        self.close()

    def send(self):
        report = self.ui.textEdit.toPlainText()
        report = list(report.split('\n'))
        print(report)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persons = []
        for i in report:
            persons.append([i, timestamp])
        print(pg.insert(persons))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Report()
    application.show()

    sys.exit(app.exec())
