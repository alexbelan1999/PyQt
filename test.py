import sys

from PyQt5 import QtWidgets

import test1
from login import Ui_Login


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.info_start)

    def info_start(self):
        self.open_info = test1.Info(self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text(),
                                    self.ui.lineEdit_4.text())
        self.open_info.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Login()
    application.show()

    sys.exit(app.exec())
