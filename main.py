import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class Ui(QMainWindow):
    status = "ready"

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("calc.ui", self)

        # Adding buttons functionality

        # First buttons row
        self.cButton.clicked.connect(self.clear_output)
        self.deleteButton.clicked.connect(self.delete)
        self.modButton.clicked.connect(lambda: self.enter_operator("%"))
        self.divisionButton.clicked.connect(lambda: self.enter_operator("/"))
        # Second buttons row
        self.sevenButton.clicked.connect(lambda: self.enter_num("7"))
        self.eightButton.clicked.connect(lambda: self.enter_num("8"))
        self.nineButton.clicked.connect(lambda: self.enter_num("9"))
        self.multiplyButton.clicked.connect(lambda: self.enter_operator("*"))
        # Third buttons row
        self.fourButton.clicked.connect(lambda: self.enter_num("4"))
        self.fiveButton.clicked.connect(lambda: self.enter_num("5"))
        self.sixButton.clicked.connect(lambda: self.enter_num("6"))
        self.minusButton.clicked.connect(lambda: self.enter_operator("-"))
        # Forth buttons row
        self.oneButton.clicked.connect(lambda: self.enter_num("1"))
        self.twoButton.clicked.connect(lambda: self.enter_num("2"))
        self.threeButton.clicked.connect(lambda: self.enter_num("3"))
        self.plusButton.clicked.connect(lambda: self.enter_operator("+"))
        # Fifth buttons row
        self.zeroButton.clicked.connect(lambda: self.enter_num("0"))
        self.dotButton.clicked.connect(self.enter_dot)
        self.equalButton.clicked.connect(self.calculate_result)

        self.show()

    def enter_num(self, num):
        screen = self.outputField.text()

        if Ui.status != "calculating":
            self.outputField.setText(f'{num}')
            Ui.status = "calculating"
        else:
            self.outputField.setText(f'{screen}{num}')

    def enter_operator(self, op):
        screen = self.outputField.text()
        operators = "%/*-+"

        if self.status == "calculating":
            if screen[-1] not in operators:
                    self.outputField.setText(f'{screen}{op}')

    def clear_output(self):
        self.outputField.setText("0")
        Ui.status = "ready"

    def delete(self):
        screen = self.outputField.text()
        screen = screen[:-1]
        self.outputField.setText(f'{screen}')

    def enter_dot(self):
        screen = self.outputField.text()

        if screen[-1] != '.':
            self.outputField.setText(f'{screen}.')

    def calculate_result(self):
        try:
            screen = self.outputField.text()
            result = eval(screen)
            self.outputField.setText(str(result))
        except:
            self.outputField.setText('ERROR')
        Ui.status = "finished"

# Initialize the app
app = QApplication(sys.argv)
UIWindow = Ui()
app.exec_()
