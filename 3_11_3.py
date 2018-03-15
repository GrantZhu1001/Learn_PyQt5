#2018年3月11日 16:37:53
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider,
    QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class APP(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 820, 530)

        self.setGeometry(300, 300, 1100, 600)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))

if __name__ == '__main__':
    app = QApplication([])
    ex = APP()
    app.exit(app.exec_())