import random

# Constants
HUMAN = 'X'
CPU = 'O'

# Evaluation dictionary for improved evaluation function
eval_dict = {
    (HUMAN, HUMAN, HUMAN): -100,
    (CPU, CPU, CPU): 100,
    (HUMAN, '-', '-'): -10,
    (CPU, '-', '-'): 10,
    ('-', HUMAN, '-'): -10,
    ('-', CPU, '-'): 10,
    ('-', '-', HUMAN): -10,
    ('-', '-', CPU): 10,
    (HUMAN, HUMAN, '-'): -10,
    (CPU, CPU, '-'): 10,
    (HUMAN, '-', HUMAN): -10,
    (CPU, '-', CPU): 10,
    (HUMAN, '-', '-'): -1,  # New entry for one symbol and two empty spaces
    (CPU, '-', '-'): 1,  # New entry for one symbol and two empty spaces
}

# Initialize the board
board = ['-'] + ['-' for _ in range(9)]

# Winning lines
winning_lines = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
    (1, 5, 9), (3, 5, 7)  # Diagonals
]

def minimax(board, depth, alpha, beta, maximizing_player):
    # Base cases
    if win(board, CPU):
        return 100 - depth
    if win(board, HUMAN):
        return -100 + depth
    if Alldone(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in range(1, 10):
            if posIsfree(board, move):
                board[move] = CPU
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[move] = '-'
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for move in range(1, 10):
            if posIsfree(board, move):
                board[move] = HUMAN
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[move] = '-'
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def evaluate(board):
    score = 0

    # Check rows
    for i in range(1, 8, 3):
        symbol_count = {'X': 0, 'O': 0, '-': 0}
        for j in range(i, i+3):
            symbol_count[board[j]] += 1
        score += evaluate_line(symbol_count)

    # Check columns
    for i in range(1, 4):
        symbol_count = {'X': 0, 'O': 0, '-': 0}
        for j in range(i, i+7, 3):
            symbol_count[board[j]] += 1
        score += evaluate_line(symbol_count)

    # Check diagonals
    diagonals = [(1, 5, 9), (3, 5, 7)]
    for diagonal in diagonals:
        symbol_count = {'X': 0, 'O': 0, '-': 0}
        for pos in diagonal:
            symbol_count[board[pos]] += 1
        score += evaluate_line(symbol_count)

    return score

def evaluate_line(symbol_count):
    if symbol_count['X'] == 3:
        return -100
    elif symbol_count['O'] == 3:
        return 100
    elif symbol_count['X'] == 2 and symbol_count['-'] == 1:
        return -10
    elif symbol_count['O'] == 2 and symbol_count['-'] == 1:
        return 10
    elif symbol_count['X'] == 1 and symbol_count['-'] == 2:
        return -1
    elif symbol_count['O'] == 1 and symbol_count['-'] == 2:
        return 1
    else:
        return 0


def CPUturn(difficulty):
    if difficulty == 'easy':
        return random.choice(get_free_positions(board))
    elif difficulty == 'medium':
        best_score = float('-inf')
        best_move = None
        for move in get_free_positions(board):
            board[move] = CPU
            score = evaluate(board)
            board[move] = '-'
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
    elif difficulty == 'hard':
        best_score = float('-inf')
        best_move = None
        for move in get_free_positions(board):
            board[move] = CPU
            score = minimax(board, 0, float('-inf'), float('inf'), False)
            board[move] = '-'
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

def get_free_positions(board):
    return [pos for pos in range(1, 10) if board[pos] == '-']

def posIsfree(board, pos):
    return board[pos] == '-'

def win(board, player):
    return any(all(board[pos] == player for pos in line) for line in winning_lines)

def Alldone(board):
    return '-' not in board[1:]

def humanturn():
    while True:
        pos = input("Choose a position to place your symbol (1-9): ")
        if pos.isdigit():
            pos = int(pos)
            if pos in range(1, 10) and posIsfree(board, pos):
                putOnBoard(HUMAN, pos)
                break
        print("Invalid position. Try again.")

def putOnBoard(symb, pos):
    board[pos] = symb

def Board(board):
    print("---------")
    print("|", board[1], board[2], board[3], "|")
    print("|", board[4], board[5], board[6], "|")
    print("|", board[7], board[8], board[9], "|")
    print("---------")

def game():
    while True:
        difficulty = input("Select difficulty level (easy, medium, hard): ")
        if difficulty in ['easy', 'medium', 'hard']:
            break
        print("Invalid difficulty level. Try again.")

    print("Tic Tac Toe - Difficulty: ", difficulty)

    while not Alldone(board):
        if not win(board, CPU):
            humanturn()
            Board(board)
        else:
            print("CPU wins!")
            break

        if not win(board, HUMAN):
            move = CPUturn(difficulty)
            if move is not None:
                putOnBoard(CPU, move)
                print("CPU picks position", move)
                Board(board)
            else:
                print("Draw!")
                break
        else:
            print("Human wins!")
            break

game()
