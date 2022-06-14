from PyQt5 import uic, QtCore, QtWidgets, QtGui
import random

class Joken_po(QtWidgets.QMainWindow):
	listChoose = ['ROCK', 'PAPER', 'SCISSORS']
	choose = ''

	def __init__(self):
		super(Joken_po, self).__init__()

		# SET WINDOW
		self.window_jogo_joken = uic.loadUi('../widgets/jogo_joken_po.ui', self)

		# SET WINDOW OPTIONS
		title = "JOKEN-PO"
		self.setWindowTitle(title)
		self.setWindowIcon(QtGui.QIcon('../img/favicon.png'))
		self.window_jogo_joken.setFixedSize(self.size())

		# FIXED BACKGROUND
		qImg = QtGui.QImage('../img/joken-po.png')
		pixmap = QtGui.QPixmap.fromImage(qImg)
		self.wrapper.setPixmap(pixmap)
		self.window()

		# SET DEFAULT HANG BUTTONS
		self.btn_pedra.clicked.connect(self.pedra_click)
		self.btn_papel.clicked.connect(self.papel_click)
		self.btn_tesoura.clicked.connect(self.tesoura_click)

		# SET RESET BUTTON
		self.btn_reset.clicked.connect(self.reset)

		# SET COUNT VARIABLES
		self.playerCount = 0
		self.computerCount = 0

		# SET RANDOM CHOICE
		self.__sort()

	# RESET GAME
	def reset(self):
		self.btn_pedra.setEnabled(True)
		self.btn_tesoura.setEnabled(True)
		self.btn_papel.setEnabled(True)
		print(f"YOU: {self.playerCount} | PC: {self.computerCount}")
		Joken_po.__sort()

	# VERIF WIN CONDITION
	def verifWin(self):
		if self.choose == 'ROCK' and Joken_po.choose == 'SCISSORS':
			self.response.setText("YOU WIN")
			self.playerCount += 1
		elif self.choose == 'ROCK' and Joken_po.choose == 'SCISSORS':
			self.response.setText("PC WIN")
			self.computerCount += 1
		elif self.choose == 'SCISSORS' and Joken_po.choose == 'PAPER':
			self.response.setText("YOU WIN")
			self.playerCount += 1
		elif self.choose == 'PAPER' and Joken_po.choose == 'SCISSORS':
			self.response.setText("PC WIN")
			self.computerCount += 1
		elif self.choose == 'PAPAR' and Joken_po.choose == 'ROCK':
			self.response.setText("YOU WIN")
			self.playerCount += 1
		elif self.choose == 'ROCK' and Joken_po.choose == 'PAPER':
			self.response.setText("PC WIN")
			self.computerCount += 1
		elif self.choose == 'ROCK' and Joken_po.choose == 'ROCK':
			self.response.setText("DRAW")
		elif self.choose == 'SCISSORS' and Joken_po.choose == 'SCISSORS':
			self.response.setText("DRAW")
		elif self.choose == 'PAPER' and Joken_po.choose == 'PAPER':
			self.response.setText("DRAW")
		self.btn_pedra.setEnabled(False)
		self.btn_papel.setEnabled(False)
		self.btn_tesoura.setEnabled(False)


	# BUTTON CLICKS
	def pedra_click(self):
		self.choose = 'ROCK'
		self.verifWin()

	def papel_click(self):
		self.choose = 'PAPER'
		self.verifWin()

	def tesoura_click(self):
		self.choose = 'SCISSORS'
		self.verifWin()

	@staticmethod
	def __sort():
		__class__.choose = random.choice(Joken_po.listChoose)
		print(f'RANDOM CHOICE: {Joken_po.choose}')

