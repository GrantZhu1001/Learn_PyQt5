from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
    QFormLayout, QLabel, QLineEdit, QTextEdit)

class APP(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        formLayout = QFormLayout()

        nameLabel = QLabel('姓名')
        nameLineEdit = QLineEdit()

        introductionLabel = QLabel('简介')
        introductionEdit = QTextEdit()

        formLayout.addRow(nameLabel, nameLineEdit)
        formLayout.addRow(introductionLabel, introductionEdit)

        self.setWindowTitle('FormLayout')
        self.setGeometry(300, 300, 300, 200)
        self.setLayout(formLayout)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    ex = APP()
    print(app.exec_())  #0
    app.exit(app.exec_())


