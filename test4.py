import glob
import os
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import test2
from progressbar import Ui_Progress_training


class Progress_training(QtWidgets.QMainWindow):
    file = ""
    dir = ""
    progress_training_info = []

    def __init__(self, info=["", "", "", ""], file = "", dir = ""):
        super(Progress_training, self).__init__()
        self.ui = Ui_Progress_training()
        self.ui.setupUi(self)
        Progress_training.progress_training_info = info
        Progress_training.file = file
        Progress_training.dir = dir
        print()
        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.progress()

    def back_menu(self):
        self.open_menu = test2.Menu(Progress_training.progress_training_info)
        self.open_menu.show()
        self.close()

    def progress(self):
        #TODO work with folder name
        path = Progress_training.dir + "*"
        files = len(glob.glob(path))
        number = 0
        for file in glob.glob(path):
            #time.sleep(5)
            print(file)
            self.ui.progressBar.setValue(round(number/files) * 100)
            number += 1
            if round(number/files) == 1:
                self.ui.pushButton_exit.setDisabled(False)
                self.ui.pushButton_menu.setDisabled(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Progress_training()
    application.show()

    sys.exit(app.exec())
