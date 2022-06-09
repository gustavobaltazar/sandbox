from Jogo_velha import *
from src.Forca import *
import sys


class First(QtWidgets.QMainWindow):
	def __init__(self):
		super(First, self).__init__()
		uic.loadUi('../widgets/janela_principal.ui', self)
		self.pushButton.clicked.connect(self.abre_jogo_forca)
		self.pushButton_2.clicked.connect(self.abre_jogo_velha)
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
		# Puxar arquivo do JokenPo
		pass


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = First()
	window.show()
	app.exec()
