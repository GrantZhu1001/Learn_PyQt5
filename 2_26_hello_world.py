#2018年2月26日 18:31:41
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QToolTip, QDesktopWidget)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('微软雅黑', 10))

        self.setToolTip('我是一个<b>父窗口</b>...')
        self.resize(500, 500)
        self.setWindowTitle('I\' m a title ^_^')
        self.setWindowIcon(QIcon('研.ico'))
        self.statusBar().showMessage('I\' m a statusBar...-_-!')
        self.center()

        btn = QPushButton('点我关闭窗口哦', self)
        btn.setToolTip('我是一个<b>按钮</b>...')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.move(100, 100)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Notice',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
