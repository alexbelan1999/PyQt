import sys

from PyQt5 import QtWidgets, QtGui

import postgresql as pg
import test2
from db import Ui_DB


class DB(QtWidgets.QMainWindow):
    DB_info = []

    def __init__(self, info=["", "", "", ""]):
        super(DB, self).__init__()
        self.ui = Ui_DB()
        self.ui.setupUi(self)
        DB.DB_info = info
        model = QtGui.QStandardItemModel()
        result = pg.select()

        for i in range(len(result)):
            item1 = QtGui.QStandardItem(str(result[i][0]))
            item2 = QtGui.QStandardItem(result[i][1])
            item3 = QtGui.QStandardItem(str(result[i][2]))
            model.appendRow([item1, item2, item3])
        model.setHorizontalHeaderLabels(["id", "name", "addtime"])

        self.ui.tableView.setModel(model)
        self.ui.tableView.setColumnWidth(0, 50)
        self.ui.tableView.setColumnWidth(1, 150)
        self.ui.tableView.setColumnWidth(2, 270)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_back.clicked.connect(self.back_menu)

    def back_menu(self):
        self.open_menu = test2.Menu(DB.DB_info)
        self.open_menu.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = DB()
    application.show()

    sys.exit(app.exec())
