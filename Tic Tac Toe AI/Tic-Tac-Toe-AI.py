#Tic Tac Toe with AI
#By default your symbol is X and CPU's O
import random
import time

board = ['-' for x in range(10)]
# def toss(human):
#     time.sleep(1)
#     coin = random.randrange(1, 3)
#     if coin == 1 and human == 'heads' or coin == 2 and human == 'tails':
#         print("Human win the toss")
#         return True
#     else:
#         print("CPU win the toss")
#         return False

def putOnBoard(symb, pos):
    board[pos] = symb
def posIsfree(pos):
    return board[pos] == '-'
def Board(board):
    print("---------")
    print("|", board[1], board[2], board[3], "|")
    print("|", board[4], board[5], board[6], "|")
    print("|", board[7], board[8], board[9], "|")
    print("---------")
def win(pos, symb):
    return ((pos[1] == symb and pos[5] == symb and pos[9] == symb) or
    (pos[3] == symb and pos[5] == symb and pos[7] == symb) or
    (pos[1] == symb and pos[2] == symb and pos[3] == symb) or
    (pos[4] == symb and pos[5] == symb and pos[6] == symb) or
    (pos[7] == symb and pos[8] == symb and pos[9] == symb) or
    (pos[1] == symb and pos[4] == symb and pos[7] == symb) or
    (pos[2] == symb and pos[5] == symb and pos[8] == symb) or
    (pos[3] == symb and pos[6] == symb and pos[9] == symb))
def Alldone(board):
    if board.count('-') > 1:
        return False
    else:
        return True
def humanturn():
    run = True
    while run:
        pos = int(input("Choose position you want to go for between 1 to 9: "))
        if pos > 0 and pos < 10:
            if posIsfree(pos):
                run = False
                print(run)
                putOnBoard('X', pos)
            else:
                print("This position is occupied")
        else:
            print("Please type a number in range")

def CPUturn():
    availableMoves = [k for k, x in enumerate(board) if x == '-']
    turn = 0
    for symb in ['O', 'X']:
        for i in availableMoves:
            boardcon = board[:]
            boardcon[i] = symb
            if win(boardcon, symb):
                turn = i
                return turn
    corners = []
    for i in availableMoves:
        if i in [1, 3, 7, 9]:
            corners.append(i)
    if len(corners) > 0:
        turn = randomSelect(corners)
        return turn
    edges = []
    for i in availableMoves:
        if i in [4, 6, 2, 8]:
            edges.append(i)
    if len(edges) > 0:
        turn = randomSelect(edges)
        return turn
    if 5 in availableMoves:
        turn = 5
        return turn
    return turn

def randomSelect(list):
    listLen = len(list)
    rand = random.randrange(0, listLen)
    return list[rand]

def game():
    Board(board)
    # print("Choose Heads or Tails : ")
    # hum = input("Human choice : ")
    while not(Alldone(board)):
        # if toss(hum):
            if not(win(board, 'O')):
                humanturn()
                Board(board)
            else:
                print("CPU wins")
                break
        # else:
            if not(win(board, 'X')):
                move = CPUturn()
                if move == 0:
                    print("Draw")
                else:
                    putOnBoard('O', move)
                    print("CPU picks ", move, " position")
                    Board(board)
            else:
                print("Human wins")
                break
game()