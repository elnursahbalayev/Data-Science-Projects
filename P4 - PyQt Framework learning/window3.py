# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogBox(object):
    def setupUi(self, DialogBox):
        DialogBox.setObjectName("DialogBox")
        DialogBox.resize(289, 228)
        self.label = QtWidgets.QLabel(DialogBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 191, 81))
        self.label.setObjectName("label")

        self.retranslateUi(DialogBox)
        QtCore.QMetaObject.connectSlotsByName(DialogBox)

    def retranslateUi(self, DialogBox):
        _translate = QtCore.QCoreApplication.translate
        DialogBox.setWindowTitle(_translate("DialogBox", "Dialog"))
        self.label.setText(_translate("DialogBox", "This is the dialog box"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogBox = QtWidgets.QDialog()
    ui = Ui_DialogBox()
    ui.setupUi(DialogBox)
    DialogBox.show()
    sys.exit(app.exec_())

