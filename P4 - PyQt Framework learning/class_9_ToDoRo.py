
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_item_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_item_line_edit.setGeometry(QtCore.QRect(20, 10, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_item_line_edit.setFont(font)
        self.add_item_line_edit.setText("")
        self.add_item_line_edit.setObjectName("add_item_line_edit")
        self.add_item_push_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_item())
        self.add_item_push_button.setGeometry(QtCore.QRect(30, 80, 141, 51))
        self.add_item_push_button.setObjectName("add_item_push_button")
        self.delete_item_push_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete_item())
        self.delete_item_push_button.setGeometry(QtCore.QRect(220, 80, 131, 51))
        self.delete_item_push_button.setObjectName("delete_item_push_button")
        self.clear_all_push_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clear_all())
        self.clear_all_push_button.setGeometry(QtCore.QRect(390, 80, 121, 51))
        self.clear_all_push_button.setObjectName("clear_all_push_button")
        self.todos_list_Widget = QtWidgets.QListWidget(self.centralwidget)
        self.todos_list_Widget.setGeometry(QtCore.QRect(20, 150, 511, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.todos_list_Widget.setFont(font)
        self.todos_list_Widget.setObjectName("todos_list_Widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_item(self):
        item = self.add_item_line_edit.text()
        self.todos_list_Widget.addItem(item)
        self.add_item_line_edit.setText('')

    def delete_item(self):
        row_to_remove = self.todos_list_Widget.currentRow()
        self.todos_list_Widget.takeItem(row_to_remove)

    def clear_all(self):
        self.todos_list_Widget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoRo"))
        self.add_item_push_button.setText(_translate("MainWindow", "Add Item"))
        self.delete_item_push_button.setText(_translate("MainWindow", "Delete Item"))
        self.clear_all_push_button.setText(_translate("MainWindow", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

