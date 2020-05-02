class Player:
    board = []
    win_Con = []
    draw_flag = False

    def __init__(self):
        self.history = []
        self.input = -1
        self.name = ''
        self.symbol = ''
        self.num = -1
        self.win_flag = False

    def playerInput(self):
        while True:
            self.input = int(input(f"{self.name} input :\n"))
            print(Player.board)
            try:
                if Player.board[self.input] == 0:
                    Player.board[self.input] = self.num
                    self.history.append(self.input)
                    break
                else:
                    print('Invalid position')
            except IndexError:
                print('Index out of range')
        for win_con_ele in Player.win_Con:
            if set(win_con_ele) <= set(self.history):
                print(f"{self.name} wins")
                self.win_flag = True
                break
        if 0 not in Player.board:
            print('Draw!')
            Player.draw_flag = True


class Board:

    def __init__(self, n):
        self.n = n
        self.board_situ = [0] * (self.n ** 2)
        self.win_condition = []

    def printBoard_init(self):
        boardRow = ''
        for i in range(0, self.n ** 2):
            boardRow = boardRow + '\t|%i|' % i
            if (i + 1) % self.n == 0 and i != 0:
                boardRow = boardRow + '\n'
        print(boardRow)

    def win_Con_Gen(self):
        for i in range(0, self.n):
            win_con_ele = []
            for j in range(0, self.n):
                win_con_ele.append(self.n * j + i)
            self.win_condition.append(sorted(win_con_ele))

        for i in range(0, self.n):
            win_con_ele = []
            for j in range(0, self.n):
                win_con_ele.append(self.n * i + j)
            self.win_condition.append(sorted(win_con_ele))

        win_con_ele = []
        for i in range(0, self.n):
            win_con_ele.append(self.n * i + i)
        self.win_condition.append(sorted(win_con_ele))

        win_con_ele = []
        for i in range(1, self.n + 1):
            win_con_ele.append((self.n - 1) * i)
        self.win_condition.append(sorted(win_con_ele))

    def printBoard(self, p1sym, p2sym):
        boardRow = ''
        for i in range(0, self.n ** 2):
            if self.board_situ[i] == 0:
                boardRow = boardRow + '\t\t| |'
            elif self.board_situ[i] == 1:
                boardRow = boardRow + f'\t\t|{p1sym}|'
            elif self.board_situ[i] == 2:
                boardRow = boardRow + f'\t\t|{p2sym}|'
            if (i + 1) % self.n == 0 and i != 0:
                boardRow = boardRow + '\n'
        print(boardRow)


board_current = Board(int(input('input N :\n')))
board_current.printBoard_init()
board_current.win_Con_Gen()
Player.board = board_current.board_situ
print(Player.board)
Player.win_Con = board_current.win_condition
player1 = Player()
player1.name = input("Player1 name:\n")
player1.symbol = input("Player1 symbol:\n")
player1.num = 1

player2 = Player()
player2.name = input("Player2 name:\n")
player2.symbol = input("Player2 symbol:\n")
player2.num = 2

while True:
    player1.playerInput()
    board_current.board_situ = Player.board
    board_current.printBoard(player1.symbol, player2.symbol)
    if player1.win_flag or Player.draw_flag:
        break
    print('----------------------------------------')
    player2.playerInput()
    board_current.board_situ = Player.board
    board_current.printBoard(player1.symbol, player2.symbol)
    if player2.win_flag or Player.draw_flag:
        break
    print('----------------------------------------')
