import sys

from PyQt5 import QtWidgets

import test
from info import Ui_Info


class Info(QtWidgets.QMainWindow):
    def __init__(self, db="", user="", password="", host=""):
        super(Info, self).__init__()
        self.ui = Ui_Info()
        self.ui.setupUi(self)
        self.ui.lineEdit_db.setText(db)
        self.ui.lineEdit_user.setText(user)
        self.ui.lineEdit_password.setText(password)
        self.ui.lineEdit_host.setText(host)
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def back(self):
        self.open_login = test.Login()
        self.open_login.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Info()
    application.show()

    sys.exit(app.exec())
