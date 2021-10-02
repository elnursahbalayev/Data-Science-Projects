from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #Load the UI file
        uic.loadUi('class_17.ui', self)
        #Define our widgets
        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')

        self.button.clicked.connect(self.clicker)

        #Show the app
        self.show()

    def clicker(self):
        # self.label.setText('You pressed something')
        # Open file dialog
        fname = QFileDialog.getOpenFileName(self, 'Open File', '','All Files (*);;Python Files (*.py)')

        # Output filename to screen
        if fname:
            self.label.setText(fname[0])
# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()