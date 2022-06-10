from PyQt5 import uic, QtCore, QtWidgets, QtGui
import random

class Joken_po(QtWidgets.QMainWindow):
	escolhas = ['Pedra', 'Papel', 'Tesoura']
	escolha = ''

	def __init__(self):
		super(Joken_po, self).__init__()

		# SET WINDOW
		self.window_jogo_joken = uic.loadUi('../widgets/jogo_joken_po.ui', self)

		# SET WINDOW OPTIONS
		title = "JOKEN-PO"
		self.setWindowTitle(title)
		self.setWindowIcon(QtGui.QIcon('../imgs/favicon.png'))
		self.window_jogo_velha.setFixedSize(self.size())

		# SET DEFAULT HANG BUTTONS
		self.btn_pedra.clicked.connect(self.pedra_click)
		self.btn_papel.clicked.connect(self.papel_click)
		self.btn_tesoura.clicked.connect(self.tesoura_click)

		# SET RESET BUTTON
		self.btn_reset.clicked.connect(self.resetar)
		self.btn_pedra_2.clicked.connect(self.entrada_nome_usuario)

		# SET COUNT VARIABLES
		self.contador_pessoal = 0
		self.contador_pc = 0

		# SET RANDOM CHOICE
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
			self.contador_pessoal += 1
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

