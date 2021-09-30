
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(266, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(80, 50, 84, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 80, 67, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 120, 88, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.select())
        self.pushButton.setGeometry(QtCore.QRect(70, 160, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 190, 130, 17))
        self.label.setObjectName("label")
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.radioButton_3.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 266, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.radioButton.setChecked(True)
        #set button states
        self.radioButton.toggled.connect(lambda: self.btnstate((self.radioButton)))
        self.radioButton_2.toggled.connect(lambda: self.btnstate((self.radioButton_2)))
        self.radioButton_3.toggled.connect(lambda: self.btnstate((self.radioButton_3)))

    def btnstate(self, b):
        if b.isChecked():
            if b.text() == "Cheese":
                self.label.setText("I love Cheese")
            else:
                self.label.setText(b.text())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Pepperoni"))
        self.radioButton_2.setText(_translate("MainWindow", "Cheese"))
        self.radioButton_3.setText(_translate("MainWindow", "Mushroom"))
        self.pushButton.setText(_translate("MainWindow", "Pick Topping"))
        self.label.setText(_translate("MainWindow", "Choose your topping"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

