from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton


@Slot
def say_hello():
    print("Button Clicked, Hello!")


app = QApplication([])
button = QPushButton("Click me")

button.clicked.connect(say_hello)
button.show()
app.exec()
