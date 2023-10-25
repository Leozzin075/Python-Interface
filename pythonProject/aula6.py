from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aula 6")
        self.setFixedSize(400, 300)

        lb = QListWidget()
        lb.addItems(['item 1', 'item 2', 'item 3'])

        lb.currentItemChanged.connect(self.index_change)
        lb.currentTextChanged.connect(self.text_change)

        self.setCentralWidget(lb)


    def index_change(self, i):
        print(i.text())

    def text_change(self, a):
        print(a)






app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()