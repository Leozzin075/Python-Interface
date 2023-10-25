from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aula 8")
        self.setFixedSize(400, 300)

        self.sb = QSpinBox()
        self.sb.setMinimum(-5)
        self.sb.setMaximum(5)

        self.setCentralWidget(self.sb)

        self.sb.valueChanged.connect(self.value_changed)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, a):
        print(a)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
