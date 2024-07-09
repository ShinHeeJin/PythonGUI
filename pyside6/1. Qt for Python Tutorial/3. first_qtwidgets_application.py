from PySide6.QtWidgets import QApplication, QLabel

app = QApplication()
label = QLabel("<b><i=red>Hello World!</i></b>")
label.show()
label.resize(500, 600)
app.exec()
