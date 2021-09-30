from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(160, 80, 200, 70))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 150, 200, 70))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(160, 220, 200, 70))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.checked())
        self.pushButton.setGeometry(QtCore.QRect(120, 280, 200, 70))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 360, 201, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 43))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #set red checked by default
        # self.checkBox.setChecked(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def checked(self):
        if self.checkBox.isChecked():
            self.red = "Red"
        else:
            self.red = ""

        if self.checkBox_2.isChecked():
            self.blue = "Blue"
        else:
            self.blue = ""

        if self.checkBox_3.isChecked():
            self.green = "Green"
        else:
            self.green = ""

        self.label.setText(f'{self.red} {self.blue} {self.green}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Red"))
        self.checkBox_2.setText(_translate("MainWindow", "Blue"))
        self.checkBox_3.setText(_translate("MainWindow", "Green"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Pick a color"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

