from time import sleep
from PyQt5 import uic, QtWidgets
import pythonforca


class Third(QtWidgets.QMainWindow):
	def __init__(self):
		super(Third, self).__init__()
		self.forca = pythonforca.Forca()
		self.__randomWord = self.forca.getRandomWord()
		self.__hint = self.forca.getHint()
		self.__lp = list()
		self.__err = 0
		self.__win = 0
		self.__try = 0
		self.__life = 6
		self.window_jogo_forca = uic.loadUi('../widgets/janela_jogo_forca.ui', self)
		self.btn_enviar.clicked.connect(self.start)
		self.window_jogo_forca.show()
		self.label_5.setText(f'Dica: {self.__hint}')

	def clearData(self):
		self.__lp = list()
		self.__err = 0
		self.__win = 0
		self.__try = 0
		self.__life = 6

	def reset(self):
		self.__randomWord = self.forca.getRandomWord()
		self.label_5.setText(f'Dica: {self.forca.getHint()}')
		self.label_8.setText("PERDEU MANO")
		self.label_6.setText(str("0"))
		self.label_7.setText(str("6"))
		self.label_9.setText(str("0"))

	def start(self):
		letra_input = self.lineEdit.text()
		self.lineEdit.setText("")

		palavra_tentativa = self.forca.search(self.__randomWord, letra_input)
		print(palavra_tentativa)

		self.__try += 1
		self.label_6.setText(str(self.__try))

		self.label_8.setText(
			str(self.forca.printWord(self.__lp, self.__randomWord, letra_input, palavra_tentativa)).strip('[]').replace(
				'\'', '').replace(',', ' '))

		if palavra_tentativa == []:
			self.__err += 1
			self.__life -= 1
			self.label_7.setText(str(self.__life))
			self.label_9.setText(str(self.__err))
			if self.__err == 6:
				self.clearData()
				self.reset()
				return

		cvl = [x.upper() for x in self.__lp]
		if self.forca.winner(self.__randomWord, cvl, letra_input):
			self.label_8.setText("VOCÊ GANHOU!!!")
			sleep(2000)
			self.clearData()
		else:
			pass


def open_win_forca():
	Third()


if __name__ == '__main__':
	pass
