#2018年3月11日 15:50:11
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
    QFrame)
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.col.name())

    def setColor(self, pressed):
        source = self.sender()
        print(source)
        print(source.text())

        if pressed:     val = 255
        else:           val = 0

        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())
        print(self.col.name())
        #以“#RRGGBB”格式返回颜色的名称; 即一个“＃”字符后跟三个两位十六进制数字。
        #ff0000
        #ffff00
        #ffffff

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exit(app.exec_())

