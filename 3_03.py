#2018年3月3日 23:22:15
#Signals & slots 信号和槽及重构事件处理器
import sys
from PyQt5.QtWidgets import (QApplication, QLCDNumber, QSlider, QWidget,
    QVBoxLayout)
from PyQt5.QtCore import Qt

class APP(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber()
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setWindowTitle('我是一个标题')
        self.setGeometry(300, 300, 250, 150)
        self.show()

    def keyPressEvent(self, e):
        '''按esc退出'''
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication([])
    e = APP()
    sys.exit(app.exec_())