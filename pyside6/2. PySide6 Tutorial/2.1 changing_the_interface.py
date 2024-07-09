from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyMainWindow(QMainWindow):
    """
    https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        self.setWindowTitle("My Oneshot App")


app = QApplication()
window = MyMainWindow()
window.show()

app.exec()
