import sys

from PyQt5 import QtWidgets, QtGui

from radio import Ui_MainWindow


class radio(QtWidgets.QMainWindow):

    def __init__(self):
        super(radio, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = radio()
    application.show()

    sys.exit(app.exec())
