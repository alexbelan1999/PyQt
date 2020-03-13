import sys

from PyQt5 import QtWidgets

import test1
from login import Ui_Login


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton_info.clicked.connect(self.info_start)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def info_start(self):
        self.open_info = test1.Info(self.ui.lineEdit_db.text(), self.ui.lineEdit_user.text(),
                                    self.ui.lineEdit_password.text(),
                                    self.ui.lineEdit_host.text())
        self.open_info.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Login()
    application.show()

    sys.exit(app.exec())
