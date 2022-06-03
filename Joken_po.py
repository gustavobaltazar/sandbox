from PyQt5 import QtCore, QtGui, QtWidgets
import centralofGames
import jogo_joken_po
import random


class Menu(centralofGames.Ui_MainWindow):
    def __init__(self, menu_principal):
        self.setupUi(menu_principal)
        self.btnHangman_2.clicked.connect(self.chamar_joken_po)

    def chamar_joken_po(self):
        self.joken_po = QtWidgets.QWidget()
        self.j = Joken_po(self.joken_po)
        self.joken_po.show()


class Joken_po(jogo_joken_po.Ui_Form):
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    escolha = ''

    def __init__(self, joken_po):
        self.setupUi(joken_po)
        self.btn_pedra.clicked.connect(self.pedra_click)
        self.btn_papel.clicked.connect(self.papel_click)
        self.btn_tesoura.clicked.connect(self.tesoura_click)
        self.btn_reset.clicked.connect(self.resetar)
        self.btn_pedra_2.clicked.connect(self.entrada_nome_usuario)
        self.contador_pessoal = 0
        self. contador_pc = 0
        self.__sortear()

    def entrada_nome_usuario(self):
        self.titulo.setGeometry(QtCore.QRect(1, 30, 500, 60))
        nome_usuario = self.lineEdit.text()
        texto = "Bem vindo  " + str(nome_usuario)
        self.titulo.setText(texto)
        self.btn_pedra_2.setEnabled(False)

    def resetar(self):
        self.btn_pedra.setEnabled(True)
        self.btn_tesoura.setEnabled(True)
        self.btn_papel.setEnabled(True)
        print(f"Pontução pessoal {self.contador_pessoal} Pontuação do pc {self.contador_pc}")
        Joken_po.__sortear()


    def verificar_vitoria(self):
        if self.escolha == 'Pedra' and Joken_po.escolha == 'Tesoura':
            self.resposta.setText("Você venceu, parabéns!!!!")
            self.contador_pessoal+=1
        elif self.escolha == 'Pedra' and Joken_po.escolha == 'Tesoura':
            self.resposta.setText("Computador venceu, derrota!!!!")
            self.contador_pc += 1
        elif self.escolha == 'Tesoura' and Joken_po.escolha == 'Papel':
            self.resposta.setText("Você venceu, parabéns!!!!")
            self.contador_pessoal += 1
        elif self.escolha == 'Papel' and Joken_po.escolha == 'Tesoura':
            self.resposta.setText("Computador venceu, derrota!!!!")
            self.contador_pc += 1
        elif self.escolha == 'Papel' and Joken_po.escolha == 'Pedra':
            self.resposta.setText("Você venceu, parabéns!!!!")
            self.contador_pessoal += 1
        elif self.escolha == 'Pedra' and Joken_po.escolha == 'Papel':
            self.resposta.setText("Computador venceu, derrota!!!!")
            self.contador_pc += 1
        elif self.escolha == 'Pedra' and Joken_po.escolha == 'Pedra':
            self.resposta.setText("Empate!!!!")
        elif self.escolha == 'Tesoura' and Joken_po.escolha == 'Tesoura':
            self.resposta.setText("Empate!!!!")
        elif self.escolha == 'Papel' and Joken_po.escolha == 'Papel':
            self.resposta.setText("Empate!!!!")
        self.btn_pedra.setEnabled(False)
        self.btn_papel.setEnabled(False)
        self.btn_tesoura.setEnabled(False)

    def pedra_click(self):
        self.escolha = 'Pedra'
        self.verificar_vitoria()

    def papel_click(self):
        self.escolha = 'Papel'
        self.verificar_vitoria()

    def tesoura_click(self):
        self.escolha = 'Tesoura'
        self.verificar_vitoria()

    @staticmethod
    def __sortear():
        __class__.escolha = random.choice(Joken_po.escolhas)
        print(Joken_po.escolha)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_principal = QtWidgets.QMainWindow()
    m = Menu(menu_principal)
    menu_principal.show()
    sys.exit(app.exec_())
