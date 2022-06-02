from PyQt5 import uic, QtWidgets
import sys

class Third(QtWidgets.QMainWindow):
    def __init__(self):
        super(Third, self).__init__()
        print("Funcionou")
        self.window_jogo_forca = uic.loadUi('Widgets/janela_jogo_forca.ui', self)
        self.window_jogo_forca.show()


def open_win_forca():
    Third()

if __name__ == '__main__':
    pass
