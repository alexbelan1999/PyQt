import glob
import sys
import time

from PyQt5 import QtWidgets

import test2
from progressbar import Ui_Progress_training


class Progress_training(QtWidgets.QMainWindow):
    file = ""
    dir = ""
    progress_training_info = []

    def __init__(self, info=["", "", "", ""], file="", dir=""):
        super(Progress_training, self).__init__()
        self.ui = Ui_Progress_training()
        self.ui.setupUi(self)
        Progress_training.progress_training_info = info
        Progress_training.file = file
        Progress_training.dir = dir
        self.ui.progressBar.setValue(0)
        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_start.clicked.connect(self.start_progress)

    def back_menu(self):
        self.open_menu = test2.Menu(Progress_training.progress_training_info)
        self.open_menu.show()
        self.close()

    def start_progress(self):
        self.ui.pushButton_exit.setDisabled(True)
        self.ui.pushButton_menu.setDisabled(True)
        self.progress()

    def progress(self):
        path = Progress_training.dir + "/*"
        print(path)
        files = len(glob.glob(path))
        number = 1
        for file in glob.glob(path):
            time.sleep(2)
            self.ui.progressBar.setValue(round(number / files, 2) * 100)
            number += 1
            if number == files:
                self.ui.pushButton_exit.setDisabled(False)
                self.ui.pushButton_menu.setDisabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Progress_training()
    application.show()

    sys.exit(app.exec())
