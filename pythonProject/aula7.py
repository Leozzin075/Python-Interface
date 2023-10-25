from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aula 7")
        self.setFixedSize(400, 300)

        self.le = QLineEdit()
        self.le.setMaxLength(10)
        self.le.setPlaceholderText('Seu nome')

        self.le.returnPressed.connect(self.return_pressed)
        self.le.selectionChanged.connect(self.selection_chaged)
        self.le.textChanged.connect(self.text_chaged)
        self.le.textEdited.connect(self.text_edit)

        self.setCentralWidget(self.le)

    def return_pressed(self):
        print("Botao clicado")
        self.centralWidget().setText("Ola")

    def selection_chaged(self):
        print("mudou")
        print(self.centralWidget().selectedText())

    def text_chaged(self, s):
        print("changed")
        print(s)

    def text_edit(self, s):
        print("editou")
        print(s)







app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()