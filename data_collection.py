import numpy as np
import copy
from board import *
from legal_moves import curr_validity_check
from legal_moves import check_human_is_plyr_2
from legal_moves import validity_check
from legal_moves import make_move
from legal_moves import board_print
from legal_moves import random_turn
from legal_moves import check_win
from legal_moves import flip_board
from legal_moves import print_board
from smart_turn import *

import time
start_time = time.time()

move_counter = 0 # initialize move counter
#board = [[0 for i in range(M)] for j in range(M)]

def set_board ():
    board = make_board()
    print_board(board)
    print("You are player L for Loser >:D")
    
    M = 9
    p1 = []
    p2 = []
    count = 0
    for i in range(4):
      for j in range(4 - i):
        # board[i][j] = 1
        p1.append([i, j])
        count = count + 1
    
    # Store origin of player 1's pieces as the last element of p1
    p1.append([0, 0])
    
    count = 0
    for i in range(5, 9):
      for j in range(13 - i, 9):
        # board[i][j] = 2
        p2.append([i, j])
        count += 1
    
    # Store origin of player 2's pieces as the last element of p2
    p2.append([8, 8])
    return board, p1, p2


    
        
        

### SMART TURN
def smart_turn (): #returns 0 if draw, 1 if p1 wins, and -1 if p2 wins
    n = 1000
    won = False
    for i in range(n):#test it out with n moves for each player
        print("i is: ", i)
        x1, y1, x2, y2 = smartturn(board, LEVELS_OF_SEARCH, p1, p2)
        print(x1, y1, x2, y2)
        make_move(x1, y1, x2, y2, 1, board, p1)
        print_board(board)
        if(check_win(board, 1)):
            print("Printing board if check_win for 1")
            print_board(board)
            print(i)
            won = True
        # ### RANDOM MOVE
        # y1, x1, y2, x2 = random_turn(board, 2, p2)
        # print(y1, x1, y2, x2)
        # make_move(x1, y1, x2, y2, 2, board, p2)
        # flip_board(board, p1, p2)

        ### SMART MOVE
        flip_board(board, p1, p2)
        x1, y1, x2, y2 = smartturn(board, LEVELS_OF_SEARCH, p2, p1)
        print(x1, y1, x2, y2)
        # board_print(board)
        make_move(x1, y1, x2, y2, 2, board, p2)
        # # print_board(board)
        # print("after move")
        # board_print(board)
        # flip_board(board, p1, p2)

        if(check_win(board, 1)):
            print("yes")
            flip_board(board, p1, p2)
            if(won):
                print("draw")
                return 0, i
            else:
                print(i)
                print("p2 wins")
                print_board(board)
                return -1, i
        if(won):
            print("won")
            flip_board(board, p1, p2)
            print("p1 wins")
            print_board(board)
            print(board)
            return 1, i
            
        flip_board(board, p1, p2)
        # print_board(board)
        # board_print(board)
    print_board(board)
    return -100


k = 1
win1 = 0
win2 = 0
draw = 0
sum1 = 0
sum2 = 0
sum_draw = 0
for i in range(k):
    board, p1, p2 = set_board()
    result, num = smart_turn()
    if(result == 0):
        draw += 1
        sum_draw += num
    elif (result == 1):
        win1 += 1
        sum1 += num
    elif (result == -1):
        win2 += 1
        sum2 += num
    else:
        print("ERROR")
        break

print("# of p1 wins: ", win1)
print("# of p2 wins: ", win2)
print("# of draws: ", draw)
if(sum1 == 0):
    print("average # turns for p1 wins ", 0)
else:
    print("average # turns for p1 wins ", (sum1)/win1)
if(sum2 == 0):
    print("average # turns for p1 wins ", 0)
else:
    print("average # turns for p2 wins ", (sum2)/win2)
if(draw == 0):
    print("average # turns for draws ", 0)
else:
    print("average # turns for draws ", (sum_draw)/draw)
print_board(board)


print("--- %s seconds ---" % (time.time() - start_time))
