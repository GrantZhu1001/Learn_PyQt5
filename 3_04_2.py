#2018年3月4日 14:49:06
#字体选择框

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
    QSizePolicy, QLabel, QFontDialog)
#该QSizePolicy类是描述水平和垂直大小调整的政策布局属性

class APP(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        #setSizePolicy通俗点说就是组件大小设置，这里设置是Fixed(不变，不随窗口大小而改变)
        #也可以设置成其他的，如：Minimum, Maximum, Expanding等等，看Qt文档
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(120, 20)
        btn.clicked.connect(self.showDialog)

        vbox.addWidget(btn)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(200, 120)

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font Dialog')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':
    app = QApplication([])
    ex = APP()
    sys.exit(app.exec_())