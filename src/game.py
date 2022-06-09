class mainGame:
    def __init__(self, posX, posO):
        self.posX = list()
        self.posO = list()
        self.__toggleVerif = 0
        self.__win = 0
        self.__p1 = 0
        self.__p2 = 0

        self.game = [['*', '*', '*'],
                     ['*', '*', '*'],
                     ['*', '*', '*']]

    def printWinner(self):
        print("Congratulations, you win!!!")

    def printTable(self):
        print("\n")
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.game[i][j], "\t", end="")
                if j < 2:
                    print("|", "\t", end="")
            print("\n", end="")

    def verif(self, pos):
        if self.game[pos[0]][pos[1]] == '*':
            return 1
        else:
            return 0

    def validChar(self, letter):
        if letter == 'O' or letter == 'X':
            return True
        else:
            return False

    def winLine(self):
        self.__win = 0
        for i in range(0, 3):
            for j in range(0, 2):
                if self.validChar(self.game[i][j]) and self.game[i][j] == self.game[i][j+1]:
                    self.__win += 1
                if self.__win == 2:
                    return 1
            return 0
        return 0

    def winColumn(self):
        self.__win = 0
        for i in range(0, 3):
            for j in range(0, 2):
                if self.validChar(self.game[j][i]) and self.game[j][i] == self.game[j + 1][i]:
                    self.__win += 1
                if self.__win == 2:
                    return 1
            return 0
        return 0

    def winDiagPrincipal(self):
        self.__win = 0
        for i1 in range(0, 2):
            if self.validChar(self.game[i1][i1]) and self.game[i1][i1] == self.game[i1 + 1][i1 + 1]:
                self.__win += 1
            if self.__win == 2:
                return 1
        return 0

    def winDiagSecondary(self):
        self.__win = 0
        for i2 in range(0, 2):
            if self.validChar(self.game[i2][3 - i2 - 1]) and self.game[i2][3 - i2 - 1] == self.game[i2 + 1][3 - i2 - 2]:
                self.__win += 1
            if self.__win == 2:
                return 1
        return 0

    def setPos(self, pos, player):
        self.game[pos[0]][pos[1]] = player
