import sys

from PyQt5 import QtWidgets

import test
import test1
import test3
from menu import Ui_Menu


class Menu(QtWidgets.QMainWindow):
    menu_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Menu, self).__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        Menu.menu_info = info
        self.ui.pushButton_info.clicked.connect(self.start_info)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_training.clicked.connect(self.start_training)

    def back(self):
        self.open_login = test.Login()
        self.open_login.show()
        self.close()

    def start_info(self):
        self.open_info = test1.Info(Menu.menu_info)
        self.open_info.show()
        self.close()

    def start_training(self):
        self.open_training = test3.Training(Menu.menu_info)
        self.open_training.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Menu()
    application.show()

    sys.exit(app.exec())
