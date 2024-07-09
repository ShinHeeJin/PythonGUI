import random
import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class MyWidget(QWidget):
    """
    https://doc.qt.io/qtforpython-6/tutorials/index.html
    """

    def __init__(self):
        super().__init__()

        self.button = QPushButton("Click!")
        self.text = QLabel("Hello World", alignment=Qt.AlignmentFlag.AlignCenter)

        self.total_layout = QVBoxLayout(self)
        self.total_layout.addWidget(self.text)
        self.total_layout.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(["Apple", "Banna", "Orange"]))


if __name__ == "__main__":
    app = QApplication()
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
