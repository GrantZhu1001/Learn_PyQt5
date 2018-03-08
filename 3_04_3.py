#2018年3月5日 23:00:23
#文件对话框   只能打开几十行代码的文件，一百多行的直接崩溃。。。
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit,
    QAction, QFileDialog)
from PyQt5.QtGui import QIcon

class Tire(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('open new file')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'home')
        #print(type(fname))     <class 'tuple'>
        #print(type(fname[0]))  <class 'str'>
        #print(type(fname[1]))  <class 'str'>
        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication([])
    ex = Tire()
    sys.exit(app.exec_())
