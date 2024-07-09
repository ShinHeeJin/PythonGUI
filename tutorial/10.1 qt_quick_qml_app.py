import sys

from PySide6.QtQuick import QQuickView
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication()
    view = QQuickView()

    view.setSource("10.2 view.qml")
    view.show()

    sys.exit(app.exec())
