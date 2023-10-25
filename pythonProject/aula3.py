from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aula 3")

        widget = QLabel("Aula 05")
        font = widget.font()
        font.setPointSize(25)
        widget.setFont(font)

        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setFixedSize(QSize(800, 600))
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
