from PySide2.QtWidgets import QApplication, QWidget
import sys

#voce precisa de apenas uma instacia por situaçao
app = QApplication(sys.argv)
#criaçao do qwidget q sera a janela
window = QWidget()
#comeca o evento em loop
window.show()
app.exec_()