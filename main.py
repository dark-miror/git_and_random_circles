import sys
from random import randint

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(20, 20, 85, 26))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Рисовать"))


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.flag = False

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')
        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.figure()
            self.qp.end()

    def figure(self):
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(50, self.width() // 5)
        x, y = randint(100 + a, self.width() - a), randint(100 + a, self.height() - a)
        self.qp.drawEllipse(x - a // 2, y - a // 2, a, a)
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.showMaximized()
    sys.exit(app.exec())
