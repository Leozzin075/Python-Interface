from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aula 9")
        self.setFixedSize(400, 300)
        slider = QSlider
        slider.setMinimum(-10)
        slider.setMaximum(10)
        slider.setSingleStep(3)

        self.setCentralWidget(slider)

        slider.valueChanged.connect(self.value_changed)
        slider.sliderPosition.connect(self.slider_position)


    def value_changed(self,i):
        print(i)

    def slider_position(self,p):
        print(p)

    def slider_pressed(self):
        print("pressed")

    def slider_released(self):
        print("released")






app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()