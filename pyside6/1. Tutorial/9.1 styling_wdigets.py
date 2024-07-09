import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            menu_widget.addItem(item)

        text_widget = QLabel("_placeholder")
        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, stretch=1)
        layout.addWidget(main_widget, stretch=5)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication()
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    with open("./ui/style2.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
