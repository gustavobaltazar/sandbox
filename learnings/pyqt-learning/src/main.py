from Jogo_velha import *
from Forca import *
from Joken_po import *
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui
import sys

class First(QtWidgets.QMainWindow):
	def __init__(self):
		super(First, self).__init__()

		# LOAD UI
		ui = uic.loadUi('../widgets/janela_principal.ui', self)

		# SET WINDOW OPTIONS
		title = "GAME HUB"
		self.setWindowTitle(title)
		self.setWindowIcon(QtGui.QIcon('../img/favicon.png'))
		ui.setFixedSize(self.size())

		# SET CLICK OPTION
		self.pushButton.clicked.connect(self.abre_jogo_velha)
		self.pushButton_2.clicked.connect(self.abre_jogo_forca)
		self.pushButton_3.clicked.connect(self.abre_jogo_jokenpo)

		# SHORTCUT SET
		self.pushButton.setShortcut("1")
		self.pushButton_2.setShortcut("2")
		self.pushButton_3.setShortcut("3")

		# ANIMATED GIF
		self.movieSet = QMovie('../gif/bg.gif')
		self.wrapper.setMovie(self.movieSet)
		self.movieSet.start()
		self.window()

	def abre_jogo_velha(self):
		window2 = Second()
		window2.window_jogo_velha.show()
		window.hide()

	def abre_jogo_forca(self):
		window3 = Third()
		window3.window_jogo_forca.show()
		window.hide()

	def abre_jogo_jokenpo(self):
		window4 = Joken_po()
		window4.window_jogo_joken.show()
		window.hide()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = First()
	window.show()
	app.exec()
