import sys

from PyQt5 import QtWidgets

import test2
from info import Ui_Info


class Info(QtWidgets.QMainWindow):
    info_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Info, self).__init__()
        self.ui = Ui_Info()
        self.ui.setupUi(self)
        Info.info_info = info
        self.ui.lineEdit_db.setText(info[0])
        self.ui.lineEdit_user.setText(info[1])
        self.ui.lineEdit_password.setText(info[2])
        self.ui.lineEdit_host.setText(info[3])
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def back(self):
        self.open_menu = test2.Menu(Info.info_info)
        self.open_menu.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Info()
    application.show()

    sys.exit(app.exec())
