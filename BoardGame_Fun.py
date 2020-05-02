def printboard_init(board, n):
    boardrow = ''
    for i in range(0, n ** 2):
        boardrow = boardrow + '\t|%i|' % i
        if (i + 1) % n == 0 and i != 0:
            boardrow = boardrow + '\n'
    print(boardrow)


def printboard(board, n):
    boardrow = ''
    for i in range(0, n ** 2):
        if board[i] == 0:
            boardrow = boardrow + '\t\t| |'
        elif board[i] == 1:
            boardrow = boardrow + '\t\t|O|'
        elif board[i] == 2:
            boardrow = boardrow + '\t\t|X|'
        if (i + 1) % n == 0 and i != 0:
            boardrow = boardrow + '\n'
    print(boardrow)


def check(list_in, win_con):
    list_in = sorted(list_in)
    if list_in in win_con:
        return True
    else:
        return False


def listmerge(list_1, list_2, board):
    for i in list_1:
        board[i] = 1
    for i in list_2:
        board[i] = 2
    return board


def validdetect(board, position):
    if board[position] == 0:
        return True
    else:
        return False


def win_Con_Gen(n):
    win_con = []
    for i in range(0, n):
        win_con_ele = []
        for j in range(0, n):
            win_con_ele.append(n * j + i)
        win_con.append(win_con_ele)

    for i in range(0, n):
        win_con_ele = []
        for j in range(0, n):
            win_con_ele.append(n * i + j)
        win_con.append(win_con_ele)

    win_con_ele = []
    for i in range(0, n):
        win_con_ele.append(n * i + i)
    win_con.append(win_con_ele)

    win_con_ele = []
    for i in range(1, n + 1):
        win_con_ele.append((n - 1) * i)
    win_con.append(win_con_ele)
    return win_con


print("P1 = O", "P2 = X")
n = int(input('input N:\n'))
board_init = [0] * (n ** 2)
board = [0] * (n ** 2)
printboard_init(board, n)
win_con = win_Con_Gen(n)
list_p1 = []
list_p2 = []
while True:
    while True:
        player1input = int(input("P1 input:\n"))
        print('----------')
        if validdetect(board, player1input):
            break
        else:
            print("invalid position")
    list_p1.append(player1input)
    board = listmerge(list_p1, list_p2, board_init)
    printboard(board, n)
    print('----------')
    if check(list_p1, win_con):
        print('p1 wins')
        break

    while True:
        player2input = int(input("P2 input:\n"))
        print('----------')
        if validdetect(board, player2input):
            break
        else:
            print("invalid position")
    list_p2.append(player2input)
    board = listmerge(list_p1, list_p2, board_init)
    printboard(board, n)
    print('----------')
    if check(list_p2, win_con):
        print('p2 wins')
        break
