import sys

from PyQt5 import QtWidgets
from hello import Ui_Hello

class Hello(QtWidgets.QMainWindow):
    def __init__(self):
        super(Hello, self).__init__()
        self.ui = Ui_Hello()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Hello()
    application.show()

    sys.exit(app.exec())

