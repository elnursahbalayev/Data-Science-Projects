import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle('Hello World')

        # Set layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Hello World, What's your name")

        # Change font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        #create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName('inputbox')
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #create a button
        my_button = qtw.QPushButton('Press Me!', clicked = lambda: press_it())
        my_button.setObjectName('pushbutton')
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            my_label.setText(f'Hello {my_entry.text()}')
            my_entry.setText('')
app = qtw.QApplication([])
window = MainWindow()

app.exec_()