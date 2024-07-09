from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyMainWindow(QMainWindow):
    """
    https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
    """

    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.button_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def button_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication()
window = MyMainWindow()
window.show()

app.exec()
