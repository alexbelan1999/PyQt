import sys

from PyQt5 import QtWidgets

import test
from menu import Ui_Menu


class Menu(QtWidgets.QMainWindow):
    def __init__(self, db="", user="", password="", host=""):
        super(Menu, self).__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def back(self):
        self.open_login = test.Login()
        self.open_login.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Menu()
    application.show()

    sys.exit(app.exec())
