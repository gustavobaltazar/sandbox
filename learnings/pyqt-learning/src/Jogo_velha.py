from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QMovie, QFont
from PyQt5 import QtGui
from game import mainGame
import sys


class Second(QtWidgets.QMainWindow):
	def __init__(self):
		super(Second, self).__init__()

		# START WINDOW AND SHOW
		self.window_jogo_velha = uic.loadUi('../widgets/janela_jogo_velha.ui', self)
		self.window_jogo_velha.show()

		# SET WINDOW OPTIONS
		title = "JOGO DA MAIS IDOSA"
		self.setWindowTitle(title)
		self.setWindowIcon(QtGui.QIcon('../img/favicon.png'))
		self.window_jogo_velha.setFixedSize(self.size())

		# FIXED BACKGROUND
		qImg = QtGui.QImage('../img/velha.png')
		pixmap = QtGui.QPixmap.fromImage(qImg)
		self.wrapper.setPixmap(pixmap)
		self.window()

		# INITIAL DEFINE
		self.console_label.setText("")

		self.bOne = self.findChild(QPushButton, 'one')
		self.bTwo = self.findChild(QPushButton, 'two')
		self.bThree = self.findChild(QPushButton, 'three')
		self.bFour = self.findChild(QPushButton, 'four')
		self.bFive = self.findChild(QPushButton, 'five')
		self.bSix = self.findChild(QPushButton, 'six')
		self.bSeven = self.findChild(QPushButton, 'seven')
		self.bEight = self.findChild(QPushButton, 'eight')
		self.bNine = self.findChild(QPushButton, 'nine')

		# BUTTON CLICK
		self.one.clicked.connect(lambda: self.startGame(self.one, self.bOne))
		self.two.clicked.connect(lambda: self.startGame(self.two, self.bTwo))
		self.three.clicked.connect(lambda: self.startGame(self.three, self.bThree))
		self.four.clicked.connect(lambda: self.startGame(self.four, self.bFour))
		self.five.clicked.connect(lambda: self.startGame(self.five, self.bFive))
		self.six.clicked.connect(lambda: self.startGame(self.six, self.bSix))
		self.seven.clicked.connect(lambda: self.startGame(self.seven, self.bSeven))
		self.eight.clicked.connect(lambda: self.startGame(self.eight, self.bEight))
		self.nine.clicked.connect(lambda: self.startGame(self.nine, self.bNine))

		# GAME VARIABLES
		self.game = mainGame([], [])
		self.alreadyPlaying = True
		self.countPlays = 0
		self.countLine = 0
		self.countColumns = 0
		self.game.printTable()

		# LINE ONE
		self.one = [0, 0]
		self.two = [0, 1]
		self.three = [0, 2]

		# LINE TWO
		self.four = [1, 0]
		self.five = [1, 1]
		self.six = [1, 2]

		# LINE THREE
		self.seven = [2, 0]
		self.eight = [2, 1]
		self.nine = [2, 2]

	def setCharClicked(self, buttonPos, buttonRef):
		buttonRef.setStyleSheet("background:rgba(255,255,255,1);\nborder: 1px solid black;")
		buttonRef.setFont(QFont('MS Shell Dlg 2', 35))
		buttonRef.setText(f'{self.game.game[buttonPos[0]][buttonPos[1]]}')

	def buttonWrapper(self, pos, buttonSelected):
		if self.game.verif(pos) == 0:
			self.setCharClicked(pos, buttonSelected)


	def startGame(self, pos, buttonObj):
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
				self.buttonWrapper(pos, buttonObj)
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
				self.buttonWrapper(pos, buttonObj)

		# WIN FUNCTIONS
		if self.game.winLine() == 1 or self.game.winColumn() == 1:
			self.console_label.setText("YOU WIN")
		elif self.game.winDiagPrincipal() == 1 or self.game.winDiagSecondary() == 1:
			self.console_label.setText("YOU WIN")
		elif self.countPlays == 8:
			self.console_label.setText("DRAW")


if __name__ == '__main__':
	pass
