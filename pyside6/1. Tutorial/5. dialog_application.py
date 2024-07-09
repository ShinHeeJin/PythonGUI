import sys

from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout


class Form(QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("My Form")

        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print(f"Hello {self.edit.text()}")


if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    form.show()

    sys.exit(app.exec())
