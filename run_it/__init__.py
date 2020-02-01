import sys
from PySide2.QtWidgets import QApplication
from .main_widget import MainWidget


def create_app():
    app = QApplication([])

    widget = MainWidget()
    widget.resize(1200, 800)
    widget.show()

    app.exit(app.exec_())
