import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
    QPushButton, QLCDNumber)

class APP(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber()

        grid = QGridLayout()
        grid.addWidget(self.lcd, 0, 0, 3, 4)
        self.setLayout(grid)

        names = ['Cls', 'Bck', 'Open', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i, j) for i in range(3, 9) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue

            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.clicked)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 150, 500, 400)
        self.show()

    def clicked(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '+', '=']
        if sender in ls:
            self.lcd.display('TEST')
        else:
            self.lcd.display(sender)

if __name__ == '__main__':
    app = QApplication([])
    ex = APP()
    sys.exit(app.exec_())