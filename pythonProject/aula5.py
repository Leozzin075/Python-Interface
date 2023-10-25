from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aula 5")
        self.setFixedSize(400, 300)

        self.widget = QComboBox()
        self.widget.addItems(['item 1', 'item 2', 'item 3'])

        self.widget.currentIndexChanged.connect(self.index_change)

        self.widget.currentTextChanged.connect(self.text_change)

        self.setCentralWidget(self.widget)


    def index_change(self, i):
        print(i)

    def text_change(self, s):
        print(s)





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()