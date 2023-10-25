from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import QSize
import sys


# importando os dados para criar um painel/executavel a cima


#logo em baixo temos a classe principal
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #colocando nome na janela
        self.setWindowTitle("Meu primeiro app")
        #criando um botao
        self.button = QPushButton("Aqui")
        #deixando fixo o tamanho da pagina
        self.setFixedSize(QSize(800, 600))
        #centralizando o botao
        self.setCentralWidget(self.button)

        #conectando o botao a funçao desejada
        self.button.clicked.connect(self.clique_botao)


#funçao para usar o botao
    def clique_botao(self):
        print("Parabens")
        #deixando o botao clicavel apenas uma vez
        self.button.setEnabled(False)
        #quando o botao é clicado ele muda o titulo da pagina
        self.setWindowTitle("Aqui mudou ein!!!!!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
