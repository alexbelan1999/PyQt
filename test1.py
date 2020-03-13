import sys

from PyQt5 import QtWidgets

from info import Ui_Info


class Info(QtWidgets.QMainWindow):
    def __init__(self, db, user, password, host):
        super(Info, self).__init__()
        self.ui = Ui_Info()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(db)
        self.ui.lineEdit_2.setText(user)
        self.ui.lineEdit_3.setText(password)
        self.ui.lineEdit_4.setText(host)
        print(db, " ", user, " ", password, " ", host)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Info()
    application.show()

    sys.exit(app.exec())
