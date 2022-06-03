from PyQt5 import uic, QtWidgets
import sys


class Second(QtWidgets.QMainWindow):
	def __init__(self):
		super(Second, self).__init__()
		print("robertin")
		self.window_jogo_velha = uic.loadUi('Widgets/janela_jogo_velha.ui', self)
		self.window_jogo_velha.show()


def openWin():
	Second()

if __name__ == '__main__':
	pass
