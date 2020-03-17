import sys

from PyQt5 import QtWidgets

import test2
from rec1 import Ui_Rec1


class Rec1(QtWidgets.QMainWindow):
    rec1_info = []

    def __init__(self, info=["", "", "", ""]):
        super(Rec1, self).__init__()
        self.ui = Ui_Rec1()
        self.ui.setupUi(self)
        Rec1.rec1_info = info
        self.ui.pushButton_back.clicked.connect(self.back)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def back(self):
        self.open_menu = test2.Menu(Rec1.rec1_info)
        self.open_menu.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Rec1()
    application.show()

    sys.exit(app.exec())