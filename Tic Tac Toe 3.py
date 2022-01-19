import random


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# this is the global varients:
currentPlayer = "X"
winner = None
gameRunning = True

# this is the game board:
def display_Board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# this func is for taking user input:
def userInput(board):
    while True:
        user_Spot = int(input("Select a spot 1-9: "))
        if board[user_Spot - 1] == "-":
            board[user_Spot - 1] = currentPlayer
            break
        elif print('invalide place'):
            continue

# this func is for checking if there is a win in colum
def check_Colum(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# this func is for checking if there is win in a row:
def checkRow(board):
    #check for row win
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True

# this func is for checking win in diagonals
def checkDiag(board):
    #check for diagolans win
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

# this func is for checking if there is a win:
def check_Win(board):
    global gameRunning
    if check_Colum(board):
        display_Board(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        display_Board(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        display_Board(board)
        print(f"The winner is {winner}!")
        gameRunning = False

# this func is for checking if there is tie:
def check_Tie(board):
    global gameRunning
    if "-" not in board:
        display_Board(board)
        print("The game is Tied!")
        gameRunning = False


#  this func is for switching player:
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def pc_Input(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()
            break
        else:
            continue

# after all the codes!
#lets play!

while gameRunning:
    print('lets play:')
    print('TIC')
    print('Tac')
    print('TOE!')
    display_Board(board)
    userInput(board)
    check_Win(board)
    check_Tie(board)
    switchPlayer()
    pc_Input(board)
    check_Win(board)
    check_Tie(board)