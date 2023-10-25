from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QLineEdit, QPushButton
from PySide2.QtCore import QSize, Qt
import sys
import pyshorteners


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encurtador de Link")
        self.resize(400, 300)
        layout = QVBoxLayout()

        self.frame = QFrame()
        self.btn = QPushButton(self.frame)
        self.btn.setText("Ir")
        self.link = QLineEdit(self.frame)
        self.link.setPlaceholderText("Coloque o link aqui:")
        self.result = QLineEdit(self.frame)
        

        layout.addWidget(self.link)
        layout.addWidget(self.btn)
        layout.addWidget(self.result)

        self.frame.setLayout(layout)

        self.btn.clicked.connect(self.encurtar_link)

        self.setCentralWidget(self.frame)

    def encurtar_link(self):
        short = pyshorteners.Shortener()
        novo_link = short.tinyurl.short(self.link.text())
        self.result.setText(novo_link)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
