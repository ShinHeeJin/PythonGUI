import sys

from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

data = {
    "Project A": ["file_a.py", "file_a.txt", "something.xls"],
    "Project B": ["file_b.csv", "photo.jpg"],
    "Project C": [],
}
app = QApplication()

tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

items = []
for key, values in data.items():
    values: list[str]
    item = QTreeWidgetItem([key])

    for value in values:
        ext = value.split(".")[-1].upper()
        child = QTreeWidgetItem([value, ext])
        item.addChild(child)
        item.addChild(child)

    items.append(item)

tree.insertTopLevelItems(0, items)
tree.show()
sys.exit(app.exec())
