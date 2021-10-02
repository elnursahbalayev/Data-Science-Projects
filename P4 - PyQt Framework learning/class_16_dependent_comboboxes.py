from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the UI file
        uic.loadUi('class_16.ui', self)

        #define our witgets
        self.combo1 = self.findChild(QComboBox, 'comboBox')
        self.combo2 = self.findChild(QComboBox, 'comboBox_2')
        self.label = self.findChild(QLabel, 'label')

        # Add items to the comboBox
        self.combo1.addItem('Male', ['John', 'Wes', 'Dan'])
        self.combo1.addItem('Female', ['April', 'Steph', 'Beth'])

        # Click the first dropdown
        self.combo1.activated.connect(self.clicker)
        self.combo2.activated.connect(self.clicker2)

        #show the app
        self.show()

    def clicker(self, index):
        # Clear the second box
        self.combo2.clear()
        # Do the dependent thing
        self.combo2.addItems(self.combo1.itemData(index))

    def clicker2(self):
        self.label.setText(f'You picked: {self.combo2.currentText()} - {self.combo1.currentText()}')
# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()