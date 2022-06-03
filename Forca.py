from PyQt5 import uic, QtWidgets
import sys
import pythonforca

class Third(QtWidgets.QMainWindow):
    def __init__(self):
        super(Third, self).__init__()
        print("Funcionou")
        self.forca = pythonforca.Forca()
        self.__randomWord = self.forca.randomWord()
        self.__lp = list()
        self.__err = 0
        self.__try = 0
        self.__life = 6
        self.window_jogo_forca = uic.loadUi('Widgets/janela_jogo_forca.ui', self)
        self.btn_enviar.clicked.connect(self.start)
        self.window_jogo_forca.show()

    def start(self):
        letra_input = self.lineEdit.text()
        self.lineEdit.setText("")
        palavra_tentativa = self.forca.search(self.__randomWord, letra_input)
        print(palavra_tentativa)
        self.__try += 1
        self.label_6.setText(str(self.__try))

        if palavra_tentativa == []:
            self.__err += 1
            self.__life -= 1
            self.label_7.setText(str(self.__life))
            self.label_9.setText(str(self.__err))
            if self.__err == 6:
                print(self.forca.randomWord())
                self.label_8.setText("PERDEU MANO")
                self.label_6.setText(str("0"))
                self.label_7.setText(str("6"))
                self.label_9.setText(str("0"))
                self.label_8.setText(str("DIGITE UMA LETRA"))
                return

        self.__lp = self.forca.printWord(self.__lp, self.__randomWord, letra_input, palavra_tentativa)
        self.label_8.setText(str(self.__lp).strip('[]').replace('\'', '').replace(',', ' '))

        if self.forca.winner(self.__randomWord, self.__lp, letra_input):
            self.label_8.setText("Você GANHOU!!!")
        else:
            pass


def open_win_forca():
    Third()

if __name__ == '__main__':
    pass
