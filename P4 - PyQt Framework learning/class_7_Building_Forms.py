import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle('Hello World')

        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add stuff/Widgets
        label_1 = qtw.QLabel("This is a Cool Label Row")
        label_1.setFont(qtg.QFont('Helvetica', 24))

        f_name = qtw.QLineEdit()
        l_name = qtw.QLineEdit()

        # Add rows to app
        form_layout.addRow(label_1)
        form_layout.addRow("First Name", f_name)
        form_layout.addRow('Last Name', l_name)
        form_layout.addRow(qtw.QPushButton('Press Here', clicked=lambda: press_it()))

        self.show()

        def press_it():
            label_1.setText(f'You clicked the button {f_name.text()} {l_name.text()}!')



app = qtw.QApplication([])
window = MainWindow()

app.exec_()