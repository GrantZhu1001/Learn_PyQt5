#2018年3月3日 23:22:03
#事件对象和事件发送
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLabel,QPushButton, QMainWindow)

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''两个button'''
        btn1 = QPushButton('Button 1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('Button 2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        grid = QGridLayout()
        grid.setSpacing(10)     #设置间隔10

        x = 0
        y = 0

        self.text = 'x:{0}, y:{1}'.format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)   #顶部对齐

        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        #鼠标移动坐标
        text ='x:{0}, y:{1}'.format(x, y)
        self.label.setText(text)

    def buttonClicked(self):
        sender = self.sender()  #事件源
        #self.statusBar().showMessage(self.sender().text() + ' was pressed')
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())