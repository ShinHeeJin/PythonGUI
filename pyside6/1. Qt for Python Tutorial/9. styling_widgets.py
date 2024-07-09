import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
w = QLabel("This is a placeholder text")
# w.setAlignment(Qt.AlignmentFlag.AlignCenter)
# w.setStyleSheet(
#     """
#         background-color: #262626;
#         color: #FFFFFF;
#         font-family: Titillium;
#         font-size: 18px;
#     """
# )
w.show()

with open("./ui/style.qss", "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)

sys.exit(app.exec())
