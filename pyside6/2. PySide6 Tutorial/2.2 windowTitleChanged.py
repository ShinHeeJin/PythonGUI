import random

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]


class MyMainWindow(QMainWindow):
    """
    https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/
    """

    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.button_clicked)

        self.windowTitleChanged.connect(self.window_title_changed)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        new_window_title = random.choice(window_titles)
        self.setWindowTitle(new_window_title)

    def window_title_changed(self, window_title):
        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication()
window = MyMainWindow()
window.show()

app.exec()
