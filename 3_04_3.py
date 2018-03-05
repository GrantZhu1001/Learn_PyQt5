#2018年3月5日 23:00:23
#文件对话框
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
        fname = QFileDialog.getOpenFileName(self, 'open file', 'home')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tire()
    sys.exit(app.exec_())