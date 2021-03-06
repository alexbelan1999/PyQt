import sys

from PyQt5 import QtWidgets

import test2
import test6
import test8
import webcamera
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
        self.ui.pushButton_photo.clicked.connect(self.start_rec2)
        self.ui.pushButton_video.clicked.connect(self.start_rec3)
        self.ui.pushButton_camera.clicked.connect(self.start_camera)

    def back(self):
        self.open_menu = test2.Menu(Rec1.rec1_info)
        self.open_menu.show()
        self.close()

    def start_rec2(self):
        self.open_rec2 = test6.Rec2(Rec1.rec1_info)
        self.open_rec2.show()
        self.close()

    def start_rec3(self):
        self.open_rec3 = test8.Rec3(Rec1.rec1_info)
        self.open_rec3.show()
        self.close()

    def start_camera(self):
        self.open_camera = webcamera.Camera(Rec1.rec1_info)
        self.open_camera.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Rec1()
    application.show()

    sys.exit(app.exec())
