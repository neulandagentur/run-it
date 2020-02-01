from PySide2 import QtWidgets


class Confirm(QtWidgets.QDialog):

    def __init__(self, text, *args, **kwargs):
        super(Confirm, self).__init__(*args, **kwargs)

        self.text = text
        self.setWindowTitle(self.text)

        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
