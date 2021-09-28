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
        my_label = qtw.QLabel("Pick something from the list below")

        # Change font size of label
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        # Create an combo box
        my_combo = qtw.QComboBox(editable=True, insertPolicy=qtw.QComboBox.InsertAtTop)
        ## Add items to the combo box
        my_combo.addItem('Pepperoni', 'something')
        my_combo.addItem('cheese', 1)
        my_combo.addItem('mushroom', qtw.QWidget)
        my_combo.addItem('peppers')
        my_combo.addItems(['one', 'two', 'three'])
        # Put combobox on the screen
        self.layout().addWidget(my_combo)
        # Create a button
        my_button = qtw.QPushButton('Press Me!', clicked = lambda: press_it())
        my_button.setObjectName('pushbutton')
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            my_label.setText(f'You picked {my_combo.currentText()}')
app = qtw.QApplication([])
window = MainWindow()

app.exec_()