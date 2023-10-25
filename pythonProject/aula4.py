from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aula 4")

        ck = QCheckBox("Marque se for verdadeiro")
        ck.setCheckState(Qt.Checked)
        ck.stateChanged.connect(self.show_state)
        ck.setCheckState(Qt.PartiallyChecked)

        self.setCentralWidget(ck)



    def show_state(self, s):
        print(s == Qt.Checked)    



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
