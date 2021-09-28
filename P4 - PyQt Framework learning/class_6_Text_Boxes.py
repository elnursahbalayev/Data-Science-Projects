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

        # Create an text box
        my_text = qtw.QTextEdit(lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=50,
                                placeholderText='Type Here...',
                                readOnly=False,
                                acceptRichText=True)
        self.layout().addWidget(my_text)


        # Create a button
        my_button = qtw.QPushButton('Press Me!', clicked = lambda: press_it())
        my_button.setObjectName('pushbutton')
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            my_label.setText(f'You typed {my_text.toPlainText()}')
            my_text.setPlainText('You pressed the button')
app = qtw.QApplication([])
window = MainWindow()

app.exec_()