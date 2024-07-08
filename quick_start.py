import random
import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo"]

        self.button = QPushButton("Click!")
        self.text = QLabel("Hello World", alignment=Qt.AlignmentFlag.AlignCenter)

        self.total_layout = QVBoxLayout(self)
        self.total_layout.addWidget(self.text)
        self.total_layout.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
