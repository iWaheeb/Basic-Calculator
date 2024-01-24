from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    status = "ready"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 532)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.outputField = QtWidgets.QLabel(self.centralwidget)
        self.outputField.setGeometry(QtCore.QRect(20, 5, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.outputField.setFont(font)
        self.outputField.setFrameShape(QtWidgets.QFrame.Panel)
        self.outputField.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputField.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.outputField.setObjectName("outputField")

        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clearOutput())
        self.cButton.setGeometry(QtCore.QRect(13, 113, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete())
        self.deleteButton.setGeometry(QtCore.QRect(88, 113, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")

        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterNum("9"))
        self.nineButton.setGeometry(QtCore.QRect(165, 193, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")

        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterNum("8"))
        self.eightButton.setGeometry(QtCore.QRect(90, 193, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")

        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterNum("7"))
        self.sevenButton.setGeometry(QtCore.QRect(15, 193, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")

        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterNum("6"))
        self.sixButton.setGeometry(QtCore.QRect(165, 273, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")

        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.enterNum("5"))
        self.fiveButton.setGeometry(QtCore.QRect(90, 273, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")

        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.enterNum("4"))
        self.fourButton.setGeometry(QtCore.QRect(15, 273, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")

        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterNum("3"))
        self.threeButton.setGeometry(QtCore.QRect(165, 353, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")

        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterNum("2"))
        self.twoButton.setGeometry(QtCore.QRect(90, 353, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")

        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterNum("1"))
        self.oneButton.setGeometry(QtCore.QRect(15, 353, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")

        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterNum("0"))
        self.zeroButton.setGeometry(QtCore.QRect(15, 430, 141, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")

        self.modButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterOperator("%"))
        self.modButton.setGeometry(QtCore.QRect(163, 113, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.modButton.setFont(font)
        self.modButton.setObjectName("modButton")

        self.divisionButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterOperator("/"))
        self.divisionButton.setGeometry(QtCore.QRect(238, 113, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.divisionButton.setFont(font)
        self.divisionButton.setObjectName("divisionButton")

        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterOperator("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(240, 193, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")

        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterOperator("-"))
        self.minusButton.setGeometry(QtCore.QRect(240, 273, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")

        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterOperator("+"))
        self.plusButton.setGeometry(QtCore.QRect(240, 353, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")

        self.dotButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.enterDot())
        self.dotButton.setGeometry(QtCore.QRect(165, 430, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.dotButton.setFont(font)
        self.dotButton.setObjectName("dotButton")

        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.calculateResult())
        self.equalButton.setGeometry(QtCore.QRect(240, 430, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# The calculator functionality
    def enterNum(self, num):
        screen = self.outputField.text()

        if Ui_MainWindow.status != "calculating":
            self.outputField.setText(f'{num}')
            Ui_MainWindow.status = "calculating"
        else:
            self.outputField.setText(f'{screen}{num}')

    def enterOperator(self, op):
        screen = self.outputField.text()
        operators = "%/*-+"

        if Ui_MainWindow.status == "calculating":
            if screen[-1] not in operators:
                    self.outputField.setText(f'{screen}{op}')

    def clearOutput(self):
        self.outputField.setText("0")
        Ui_MainWindow.status = "ready"

    def delete(self):
        screen = self.outputField.text()
        screen = screen[:-1]
        self.outputField.setText(f'{screen}')

    def enterDot(self):
        screen = self.outputField.text()

        if screen[-1] != '.':
            self.outputField.setText(f'{screen}.')

    def calculateResult(self):
        try:
            screen = self.outputField.text()
            result = eval(screen)
            self.outputField.setText(str(result))
        except:
            self.outputField.setText('ERROR')
        Ui_MainWindow.status = "finished"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "الحاسبة"))
        self.outputField.setText(_translate("MainWindow", "0"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.deleteButton.setText(_translate("MainWindow", "DEL"))
        self.modButton.setText(_translate("MainWindow", "%"))
        self.divisionButton.setText(_translate("MainWindow", "÷"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.multiplyButton.setText(_translate("MainWindow", "×"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
