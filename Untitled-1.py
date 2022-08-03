import random
from turtle import position

# Naughts and Crosses Board
def displayBoard(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-|-|-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-|-|-")
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-|-|-")

# player input
def playerIn():
    marker=" "
    while marker != "x" or marker != "o":
        marker = input("player must choose 'x' or 'o': ")
        
        if marker=="o":
            return print("o")

        elif marker=="x":
            return print('x')

        else:
            return print("Please input either an 'x' or a 'o'")      

# who goes first 
def firstMove():
    if random.randint(0,1) == 0:
        return "player 1 will start the game"
    else: 
        return "player 2 will start the game"

# where to move the marker
def handleTurn(board, marker, position):
    board[position] = marker

# free space for next move
def spaceFree(board, pos):
    return board[pos]==" "

# full board check
def fullBoardCheck(board):
    for i in range(1,10):
        if spaceFree(board, i):
            return False
    return True

# next move
def playerChoice(board):
    position = 0
    
    while position not in range(1,10) or not spaceFree(board, position):
        position = int(input("Choose your next position: (1-9) "))
        return position

# winner
def checkWin(board, mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark)or
    (board[4]==mark and board[5]==mark and board[6]==mark)or
    (board[1]==mark and board[2]==mark and board[3]==mark)or
    (board[7]==mark and board[4]==mark and board[1]==mark)or
    (board[8]==mark and board[5]==mark and board[2]==mark)or
    (board[9]==mark and board[6]==mark and board[3]==mark)or
    (board[7]==mark and board[5]==mark and board[3]==mark)or
    (board[9]==mark and board[5]==mark and board[1]==mark))

def replay():
    return input('Do you want to play again? [Y/N]: ')

# Run game
while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = playerIn()
    turn = firstMove()
    print (turn + " and will go first")
    
    # Game play 
    play_game = input('Are you ready to play? [Y/N]')
    if play_game == ("Y"):
        game_is_on = True
    else:
        game_is_on = False
    
    while game_is_on:
        if turn == "player 1":
            displayBoard(theBoard)
            print("player 1")
            position = playerChoice(theBoard)
            handleTurn(theBoard, player1_marker, position)

            if checkWin(theBoard, player1_marker):
                displayBoard(theBoard)
                print('Congratulations! You have won the game!')
                game_is_on = False
            else:
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'AI player'
        else:
            displayBoard(theBoard)
            print("AI player")
            position = playerChoice(theBoard)
            handleTurn(theBoard, player2_marker, position)
        





