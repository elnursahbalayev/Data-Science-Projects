from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the Ui file
        uic.loadUi('class_18.ui', self)

        # Define our widgets
        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')

        self.button.clicked.connect(self.clicker)


        # Show the app
        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '', 'All files (*)')

        # Open the image
        self.pixmap = QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)
# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()