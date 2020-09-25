#---------------------------------------------------------------
# File Name:    reversi.py
# Author:       Aprajita Bhasin
# Description:  Reversi Game
# --------------------------------------------------------------    

import copy
playerName = ['0', 'B', 'W']
posChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
posInt = ['1', '2', '3', '4', '5', '6', '7', '8']
usr = '' # quit the game when set to 'q'
playerTurn = 1

possibleDirections = [
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1]
]

def new_board():
    board = []
    # Blanks out the board it is passed, except for the original starting position.
    for i in range(8):
        board.append([' '] * 8)

    # Starting pieces:
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'
    
    return board

def print_board(board):
    # This function prints out the board that it was passed. Returns None.
    HLINE = "  +---+---+---+---+---+---+---+---+"

    print("    a   b   c   d   e   f   g   h")
    # print("    0   1   2   3   4   5   6   7")
    print(HLINE)
    for x in range(8):
        print(x+1, end=' ')
        for y in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(HLINE)

def user_input():
    player = input("Which player do you want to be (B/W):")
    if player == 'B':
        print("You are player 1.")
    elif player == 'W':
        print("You are player 2.")
    else:
        print("Wrong input. Please enter again")

def score(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'W' and 'B'.
    wscore = 0
    bscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'W':
                wscore += 1
            if board[x][y] == 'B':
                bscore += 1
    return wscore, bscore

def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <=7

def isBlank(board, x, y):
    if board[x][y] == ' ':
        return False

def getPlayerLetter(player):
    if player == 1:
        return 'B'
    else:
        return 'W'

def getOtherPlayerLetter(player):
    if player == 1:
        return 'W'
    else:
        return 'B'

def enclosing(board, player, pos, direct):
    atleast_one_other = 0
    x = pos[0]
    y = pos[1]
    dx = direct[0]
    dy = direct[1]

    newx = x
    newy = y

    while True:
        newx = newx + dx
        newy = newy + dy

        if(isOnBoard(newx, newy)):
            if (board[newx][newy] == ' '):
                return False
            
            if (player != board[newx][newy]):
                atleast_one_other = 1
                continue

            if (player == board[newx][newy]):
                if atleast_one_other == 0:
                    return False
                elif atleast_one_other == 1:
                    return True
                else:
                    print ("~~~~~ ERROR ~~~~~")
        else:
            return False


def enclosing_and_next_state(board, player, pos, direct):
    atleast_one_other = 0
    x = pos[0]
    y = pos[1]
    dx = direct[0]
    dy = direct[1]

    board[x][y] = player
    newx = x
    newy = y

    while isOnBoard(newx, newy):
        newx = newx + dx
        newy = newy + dy

        if (board[newx][newy] == ' '):
            return False
        
        if (player != board[newx][newy]):
            board[newx][newy] = player
            atleast_one_other = 1
            continue

        if (player == board[newx][newy]):
            if atleast_one_other == 0:
                return False
            elif atleast_one_other == 1:
                return True
            else:
                print ("~~~~~ ERROR ~~~~~")

def valid_moves(board, player):
    board_positions = []

    # print("Identifying valid moves for player - ",  getPlayerLetter(player))
    pl = getPlayerLetter(player)
    otherpl = getOtherPlayerLetter(player)

    for i in range(7):
        for j in range(7):
            if(board[i][j] == otherpl):
                for k in range(len(possibleDirections)):
                    rel_i = possibleDirections[k][0]
                    rel_j = possibleDirections[k][1]

                    if (board[i + rel_i][j + rel_j] == ' '):
                        if(enclosing(board, pl, [i+rel_i, j+rel_j], [rel_i*-1, rel_j*-1]) == True):
                            # print ("Valid Move", i, j, possibleDirections[k])
                            board_positions.append([i+rel_i, j+rel_j])
                        # else:
                            # print("Invalid Move", i, j, possibleDirections[k])
    
    # print(board_positions)                
    return(board_positions)


def next_state(board, player, pos):
    otherPlayer = 0
    pl = getPlayerLetter(player)
    otherpl = getOtherPlayerLetter(player)

    for k in range(len(possibleDirections)):
        if(enclosing(board, pl, pos, possibleDirections[k]) == True):
            # Convert all tiles to player in direction
            enclosing_and_next_state(board, pl, pos, possibleDirections[k])

    if(player == 1):
        otherPlayer = 2
    else:
        otherPlayer = 1

    moves = valid_moves(board, otherPlayer)
    if (len(moves) == 0):
        otherPlayer = 0
        
    return board, otherPlayer

def position(str):
    arr = [0, 0]
    pos = 0

    for i in str:
        if pos == 0:
            if i in posChar:
                arr[1] = posChar.index(i)
            pos += 1
        elif pos == 1:
            if i in posInt:
                arr[0] = posInt.index(i)
            pos += 1
        else:
            break
    
    return arr

def run_two_player():
    global playerTurn
    global main_board

    usr = input("Enter next move for player %s or 'q' to quit: " % playerTurn)

    while (usr != 'q'):
        # check if user entered valid position
        pos = position(usr)
        if (isOnBoard(pos[0], pos[1]) == False):
            print ("invalid move. move not within board")
            usr = input("Enter next move for player %s or 'q' to quit: " % playerTurn)
            continue

        moves = valid_moves(main_board, playerTurn)

        # if no more valid moves
        if (len(moves) == 0):
            print("Game Over. Scores are: W=%s, B=%s" % (score(main_board)))
            exit(0)

        if (pos in moves) == False:
            print("invalid move")
            usr = input("Enter next move for player %s or 'q' to quit: " % playerTurn)
            continue

        main_board, playerTurn = next_state(main_board, playerTurn, pos)
        print_board(main_board)

        if(playerTurn == 0):
            print("Game Over. Scores are: W=%s, B=%s" % (score(main_board)))
            exit(0)

        usr = input("Enter next move for player %s or 'q' to quit: " % playerTurn)


def run_single_player():
    global playerTurn
    global main_board

    usr = input("Enter next move for player %s or 'q' to quit: " % playerTurn)

    while (usr != 'q'):
        # check if user entered valid position
        pos = position(usr)
        if (isOnBoard(pos[0], pos[1]) == False):
            print ("invalid move. move not within board")
            usr = input("Enter next move for player %s or 'q' to quit: " % playerTurn)
            continue

        moves = valid_moves(main_board, playerTurn)

        # if no more valid moves
        if (len(moves) == 0):
            print("Game Over. Scores are: W=%s, B=%s" % (score(main_board)))
            exit(0)

        if (pos in moves) == False:
            print("invalid move")
            usr = input("Enter next move for player %s or 'q' to quit: " % playerTurn)
            continue

        main_board, playerTurn = next_state(main_board, playerTurn, pos)
        print_board(main_board)

        # make move on behalf of player 2 that will fetch max score
        moves = valid_moves(main_board, playerTurn)
        # if no more valid moves for player 2 then exit
        if (len(moves) == 0):
            print("Game Over. Scores are: W=%s, B=%s" % (score(main_board)))
            exit(0)

        #do all permutations of scoring to find max score
        max_score = 0
        max_score_index = 0
        i=0
        for a_move in moves:
            tmp_board = copy.deepcopy(main_board)
            tmp_board_2, z = next_state(tmp_board, 2, a_move)

            if(z == 0):
                print("Game Over. Scores are: W=%s, B=%s" % (score(main_board)))
                exit(0)

            scr_1, scr_2 = score(tmp_board_2) # scr_1 is score of 'W' and scr_2 is score of 'B'.
            if(max_score < scr_1):
                max_score = scr_1
                max_score_index = i
            i += 1

        main_board, playerTurn = next_state(main_board, playerTurn, moves[max_score_index])
        print_board(main_board)

        usr = input("Enter next move for player %s or 'q' to quit: " % playerTurn)



###########################
# Main Program Starts here
###########################
print("Welcome to Reversi!")
main_board = new_board()
print_board(main_board)
# # Example a
# print("Example a: W=%s, B=%s" % (score(new_board())))

# # Example b
# print("Example b: ", enclosing(new_board(), 'B', [5, 4], [-1, 0]))

# # Example c
# tmp_board, plyr = next_state(new_board(), 1, [4, 5])
# print_board(tmp_board)
# print("Example c: Next player = ", plyr)

# # Example d
# print("Example d: ", valid_moves(next_state(new_board(), 1, [4, 5])[0], 2))

# # Example e
# print("Example e: ", position("e3"))

# Reversi Game Program
plyr_count = input("Enter number of players - 1 or 2? ")

try:

    if (int(plyr_count) == 1):
        run_single_player()

    if (int(plyr_count) == 2):
        run_two_player()

except ValueError:
    print("Incorrect player count. Exiting...")
    exit(0)


print("Game Over. Scores are: W=%s, B=%s" % (score(main_board)))