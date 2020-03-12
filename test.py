import sys

from PyQt5 import QtWidgets

from login import Ui_Login
import test1

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.hello_start)

    def hello_start(self):
        self.open_hello = test1.Hello()
        self.open_hello.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Login()
    application.show()

    sys.exit(app.exec())
