import os
from PySide2 import QtWidgets
from run_it.confirm import Confirm


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.btn_add_command = QtWidgets.QPushButton('Add new shell command')
        self.btn_delete_command = QtWidgets.QPushButton('Delete new shell command')

        # attach list view with process searches
        self.list_widget = QtWidgets.QListWidget()

        # create layout
        self.layout = QtWidgets.QVBoxLayout()

        # add buttons
        self.layout.addWidget(self.btn_add_command)
        self.layout.addWidget(self.btn_delete_command)

        # add list view
        self.layout.addWidget(self.list_widget)

        # set layout
        self.setLayout(self.layout)

        # attach event listener
        self.btn_add_command.clicked.connect(self.add_item)
        self.btn_delete_command.clicked.connect(self.delete_item)

        self.list_widget.itemDoubleClicked.connect(self.run_it)


    def run_it(self, item):
        os.system(item.text())

    def add_item(self):
        item, accept = QtWidgets.QInputDialog().getText(
            self,
            'Add new command',
            'Shell command:'
        )

        if item and accept:
            list_item = QtWidgets.QListWidgetItem(item)
            self.list_widget.addItem(list_item)

    def delete_item(self):
        dialog = Confirm('Wirklich löschen?')
        current_item = self.list_widget.currentItem()

        # no item is selected
        if current_item is None:
            return

        if dialog.exec_():
            row = self.list_widget.row(current_item)
            self.list_widget.takeItem(row)
