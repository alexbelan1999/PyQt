import datetime
import sys

import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage

from camera import Ui_Camera
import  test2
import postgresql as pg

class Camera(QtWidgets.QMainWindow):
    stop = False
    camera_info = []

    def __init__(self,info=["", "", "", ""]):
        super(Camera, self).__init__()
        self.ui = Ui_Camera()
        self.ui.setupUi(self)
        Camera.camera_info = info
        self.ui.pushButton_start.clicked.connect(self.camera)
        self.ui.pushButton_stop.clicked.connect(self.stop_rec)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_menu.clicked.connect(self.back_menu)
        self.ui.pushButton_report.clicked.connect(self.report)

    def camera(self):
        self.ui.pushButton_exit.setDisabled(True)
        self.ui.pushButton_menu.setDisabled(True)
        self.ui.pushButton_report.setDisabled(True)
        video_capture = cv2.VideoCapture(0)
        Camera.stop = False
        while True:

            ret, frame = video_capture.read()
            frame = cv2.flip(frame, 1)

            cvtFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(cvtFrame, cvtFrame.shape[1], cvtFrame.shape[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)

            self.ui.textEdit.append(video_capture.getBackendName())
            self.ui.label_video.setPixmap(pix)

            key = cv2.waitKey(100)
            if Camera.stop:
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def stop_rec(self):
        self.ui.pushButton_exit.setDisabled(False)
        self.ui.pushButton_menu.setDisabled(False)
        self.ui.pushButton_report.setDisabled(False)
        Camera.stop = True

    def back_menu(self):
        self.open_menu = test2.Menu(Camera.camera_info)
        self.open_menu.show()
        self.close()

    def report(self):
        report = self.ui.textEdit.toPlainText()
        report = list(report.split('\n'))
        print(report)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        persons = []
        persons.append(["Alex", timestamp])
        print(pg.insert(persons))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Camera()
    application.show()

    sys.exit(app.exec())
