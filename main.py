import sys

from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5 import QtWidgets, QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 520, 365)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(220, 300)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        r = random.randint(1, 100)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        qp.drawEllipse(30, 30, r, r)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        qp.drawEllipse(200, 30, r, r)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        qp.drawEllipse(400, 30, r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
