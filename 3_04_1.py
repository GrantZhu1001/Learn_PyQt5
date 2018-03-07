#2018年3月4日 14:46:16
#颜色选择框
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFrame,
    QColorDialog)
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        #setStyleSheet(self, str)
        self.frm.setStyleSheet('background-color:%s' % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    sys.exit(app.exec_())