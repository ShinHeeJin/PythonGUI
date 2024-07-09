import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyMainWindow(QMainWindow):
    """
    https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))
        self.setMinimumSize
        self.setMaximumSize

        self.setCentralWidget(button)


app = QApplication()
window = MyMainWindow()
window.show()
app.exec()
