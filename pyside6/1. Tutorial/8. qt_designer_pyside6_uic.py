from PySide6.QtWidgets import QApplication, QMainWindow
from test_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QApplication([])
window = MainWindow()
window.show()

app.exec_()
