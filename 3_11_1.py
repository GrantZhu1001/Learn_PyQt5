#2018年3月11日 15:18:15
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        #每当一个可检查的按钮改变其状态时，就会发出这个信号。如果勾选按钮，检查是true，如果按钮未选中，则为false。
        cb.toggle()
        cb.stateChanged.connect(self.changetitle)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 250, 150)
        self.show()

    def changetitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('Nothing')

if __name__ == '__main__':
    app = QApplication([])
    s = Example()
    app.exit(app.exec_())