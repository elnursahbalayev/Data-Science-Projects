
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(238, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Average_Pressure_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Average_Pressure_Input.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.Average_Pressure_Input.setObjectName("Average_Pressure_Input")
        self.Bubble_Point_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Bubble_Point_Input.setGeometry(QtCore.QRect(80, 110, 113, 20))
        self.Bubble_Point_Input.setObjectName("Bubble_Point_Input")
        self.Flowing_Pressure_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Flowing_Pressure_Input.setGeometry(QtCore.QRect(80, 70, 113, 20))
        self.Flowing_Pressure_Input.setObjectName("Flowing_Pressure_Input")
        self.Average_Pressure_Label = QtWidgets.QLabel(self.centralwidget)
        self.Average_Pressure_Label.setGeometry(QtCore.QRect(20, 30, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Average_Pressure_Label.setFont(font)
        self.Average_Pressure_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Average_Pressure_Label.setObjectName("Average_Pressure_Label")
        self.Flowing_Pressure_Label = QtWidgets.QLabel(self.centralwidget)
        self.Flowing_Pressure_Label.setGeometry(QtCore.QRect(20, 70, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Flowing_Pressure_Label.setFont(font)
        self.Flowing_Pressure_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Flowing_Pressure_Label.setObjectName("Flowing_Pressure_Label")
        self.Bubble_Point_Label = QtWidgets.QLabel(self.centralwidget)
        self.Bubble_Point_Label.setGeometry(QtCore.QRect(20, 110, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bubble_Point_Label.setFont(font)
        self.Bubble_Point_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Bubble_Point_Label.setObjectName("Bubble_Point_Label")
        self.Flow_Rate_Label = QtWidgets.QLabel(self.centralwidget)
        self.Flow_Rate_Label.setGeometry(QtCore.QRect(20, 150, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Flow_Rate_Label.setFont(font)
        self.Flow_Rate_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Flow_Rate_Label.setObjectName("Flow_Rate_Label")
        self.Flow_Rate_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Flow_Rate_Input.setGeometry(QtCore.QRect(80, 150, 113, 20))
        self.Flow_Rate_Input.setObjectName("Flow_Rate_Input")
        self.Productivity_Index_Label = QtWidgets.QLabel(self.centralwidget)
        self.Productivity_Index_Label.setGeometry(QtCore.QRect(20, 190, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Productivity_Index_Label.setFont(font)
        self.Productivity_Index_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Productivity_Index_Label.setObjectName("Productivity_Index_Label")
        self.Productivity_Index_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Productivity_Index_Input.setGeometry(QtCore.QRect(80, 190, 113, 20))
        self.Productivity_Index_Input.setObjectName("Productivity_Index_Input")
        self.Direction_Label = QtWidgets.QLabel(self.centralwidget)
        self.Direction_Label.setGeometry(QtCore.QRect(0, 0, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Direction_Label.setFont(font)
        self.Direction_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Direction_Label.setObjectName("Direction_Label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.calculate())
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 238, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calculate(self):
        q = (self.Flow_Rate_Input.text())
        Pres = (self.Average_Pressure_Input.text())
        Pwf = (self.Flowing_Pressure_Input.text())
        Pb = (self.Bubble_Point_Input.text())
        J = self.Productivity_Index_Input.text()

        # Check Bubble point conditions
        if Pres > Pb and Pwf > Pb:
            # Use Straight Line IPR
            if J == '':
                q, Pres, Pwf, Pb = float(q, Pres, Pwf, Pb)
                J = q/(Pres - Pwf)
                self.Productivity_Index_Input.setText(str(np.round(J, 3)))
                self.statusbar.showMessage(f'J* found to be {J}')
            elif Pwf == '':
                Pwf = (J * Pres - q) / J
                self.Flowing_Pressure_Input.setText(str(np.round(Pwf, 3)))
                self.statusbar.showMessage(f'Pwf found to be {Pwf}')

        elif Pres > Pb and Pwf < Pb:
            pass
        elif Pres < Pb and Pwf < Pb:
            pass


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Production Engineering"))
        self.Average_Pressure_Label.setText(_translate("MainWindow", "Pres"))
        self.Flowing_Pressure_Label.setText(_translate("MainWindow", "Pwf"))
        self.Bubble_Point_Label.setText(_translate("MainWindow", "Pb"))
        self.Flow_Rate_Label.setText(_translate("MainWindow", "Q"))
        self.Productivity_Index_Label.setText(_translate("MainWindow", "J*"))
        self.Direction_Label.setText(_translate("MainWindow", "Please Enter in Field Units"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

