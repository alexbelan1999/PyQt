from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("ui/hello.ui")

win.show()
sys.exit(app.exec())
