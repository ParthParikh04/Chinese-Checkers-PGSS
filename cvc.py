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
from smart_turn import *

move_counter = 0 # initialize move counter
#board = [[0 for i in range(M)] for j in range(M)]

board = make_board()
print_board(board)
print("You are player L for Loser >:D")

M = 9
#p1 = [[0 for i in range(2)] for j in range(9)]
p1 = []
p2 = []
#board = [[0 for i in range(M)] for j in range(M)]
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

# #test it out with just 1 random move
# y1, x1, y2, x2 = random_turn(board, 1)
# make_move(x1, y1, x2, y2, 1, board, p1)

#testing out with a manual move:
# make_move(0, 2, 0, 4, 1, board, p1)
# print_board(board)

## SMART TURN
n = 100
for i in range(n):#test it out with n moves for each player
    x1, y1, x2, y2 = smartturn(board, LEVELS_OF_SEARCH, p1, p2)
    print(x1, y1, x2, y2)
    make_move(x1, y1, x2, y2, 1, board, p1)
    print(calc_board1(p1))
    
    y1, x1, y2, x2 = random_turn(board, 2, p2)
    # print(x1, y1, x2, y2)
    make_move(x1, y1, x2, y2, 2, board, p2)
    
    print_board(board)
    print(p1)
    x = input()


# ### RANDOM TURN
# n = 100
# for i in range(n):#test it out with n moves for each player
#     y1, x1, y2, x2 = random_turn(board, 1, p1)
#     print(x1, y1, x2, y2)
#     make_move(x1, y1, x2, y2, 1, board, p1)
#     print(calc_board1(p1))
    
    
#     y1, x1, y2, x2 = random_turn(board, 2, p2)
#     print(x1, y1, x2, y2)
#     make_move(x1, y1, x2, y2, 2, board, p2)
    
#     print_board(board)
#     print(p1)
#     x = input()