from PyQt5 import uic, QtWidgets
from game import mainGame
import sys


class Second(QtWidgets.QMainWindow):
	def __init__(self):
		super(Second, self).__init__()

		# START WINDOW AND SHOW
		self.window_jogo_velha = uic.loadUi('../widgets/janela_jogo_velha.ui', self)
		self.window_jogo_velha.show()

		# INITIAL DEFINE
		self.console_label.setText("")

		# BUTTON CLICK
		self.one.clicked.connect(lambda : self.startGame(self.one))
		self.two.clicked.connect(lambda : self.startGame(self.two))
		self.three.clicked.connect(lambda : self.startGame(self.three))
		self.four.clicked.connect(lambda : self.startGame(self.four))
		self.five.clicked.connect(lambda : self.startGame(self.five))
		self.six.clicked.connect(lambda : self.startGame(self.six))
		self.seven.clicked.connect(lambda : self.startGame(self.seven))
		self.eight.clicked.connect(lambda : self.startGame(self.eight))
		self.nine.clicked.connect(lambda : self.startGame(self.nine))

		# GAME VARIABLES
		self.game = mainGame([],[])
		self.alreadyPlaying = True
		self.countPlays = 0
		self.countLine = 0
		self.countColumns = 0
		self.game.printTable()

		# LINE ONE
		self.one = [0,0]
		self.two = [0,1]
		self.three = [0,2]

		# LINE TWO
		self.four = [1,0]
		self.five = [1,1]
		self.six = [1,2]

		# LINE THREE
		self.seven = [2,0]
		self.eight = [2,1]
		self.nine = [2,2]

	def pressedDown(self):
		print("Botão apertado.")

	def startGame(self, pos):
		self.countPlays += 1
		if self.alreadyPlaying:
			self.alreadyPlaying = False
			hasVerif = self.game.verif(pos)
			self.alreadyPlaying = True if not hasVerif else False
			if not hasVerif:
				self.countPlays -= 1

			if hasVerif == 0:
				self.console_label.setText("Impossível sobreescrever.")
			else:
				self.game.setPos(pos, "X")
				print("'X' JOGOU")
				self.game.printTable()
		else:
			self.alreadyPlaying = True
			hasVerif = self.game.verif(pos)
			self.alreadyPlaying = False if not hasVerif else True
			if not hasVerif:
				self.countPlays -= 1

			if hasVerif == 0:
				self.console_label.setText("Impossível sobreescrever.")
			else:
				self.game.setPos(pos, "O")
				print("'O' JOGOU")
				self.game.printTable()

		# DRAW FUNCTIONS

		if self.game.winLine() == 1 or self.game.winColumn() == 1:
			self.game.printWinner()
		elif self.game.winDiagPrincipal() == 1 or self.game.winDiagSecondary() == 1:
			self.game.printWinner()
		elif self.countPlays == 8:
			self.console_label.setText("DRAW")


if __name__ == '__main__':
	pass
