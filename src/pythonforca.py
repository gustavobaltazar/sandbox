import random

class Forca():
    def __init__(self):
        self.__palavras = {
            "Uva": "Fruta",
            "Abacaxi": "Fruta",
            "Televisao": "Eletronico",
            "Cadeira": "Exemplo do andre",
            "Robson": "Deus supremo",
            "Slime": "Rezende",
            "Computador": "Usamos o dia todo",
            "Celular": "conversar",
            "Sim": "sim",
            "Bebas": "Bobas"
        }
        self.__randomWord = self.randomWord()
        self.__err = 0
        self.__lp = list()

    def getRandomWord(self):
        self.__randomWord = self.randomWord()
        print(self.__randomWord)
        return self.__randomWord

    def getHint(self):
        hint = self.__palavras[self.__randomWord]
        print(hint)
        return hint

    def startGame(self):
        while True:
            letra = str(input("Digite a letra que você quer encontrar: ")).upper()
            iList = self.search(self.__randomWord, letra)
            print(iList)
            if iList == []:
                self.__err += 1
                if self.__err == 6:
                    print(self.randomWord())
                    break

            self.printWord(self.__lp, self.__randomWord, letra, iList)
            if self.winner(self.__randomWord, self.__lp, letra):
                break
            else:
                pass

    def randomWord(self):
        randomP = random.choice(list(self.__palavras.keys()))
        return randomP

    def winner(self, word, lp, letter):
        if lp == list(word.upper()):
            print('Ganhou')
            return True
        elif letter == word.upper():
            lp.append(word)
            print('Ganhou')
            return True
        else:
            print('Próxima jogada...')
            return False

    def printWord(self, lp, word, letter, indexList):
        for i, j in enumerate(word):
            if len(lp) != len(word):
                lp.append('_')

        for x in indexList:
            lp[x] = letter
        print(*lp)

        return lp

    def search(self, s, c):
        s = s.upper()
        c = c.upper()
        lst = []
        for pos, char in enumerate(s):
            if char == c:
                lst.append(pos)
        return lst


if __name__ == '__main__':
    game = Forca()
