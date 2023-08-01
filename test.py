import statistics


print(statistics.stdev([0, 1, 2, 3]))


'''
import numpy as np
from board import *
from legal_moves import *
from legal_moves import curr_validity_check
from legal_moves import check_human_is_plyr_2
from legal_moves import validity_check
from legal_moves import make_move
from legal_moves import board_print
from legal_moves import random_turn
from legal_moves import check_win
from legal_moves import valid_moves

#make_move(0,0,2,0,1,board, 1)
p1_2 = []
for i in range(5, 9):
  for j in range(13 - i, 9):
    board[i][j] = 2
    p1_2.append([i, j])
print(p1_2)
#function to make 1 plyaer board
def endgame_make_board():
    M = 9
    board = [[0 for i in range(M)] for j in range(M)]
    for i in range(5,9):
        for j in range(13-i, 9):
            board[i][j] = 1
    return board



board = endgame_make_board()
board_print(board)



print(board[0][0])

valid_moves(p1_2, board)
y = valid_moves(p1_2, board)
print(y)
print(y[(6,7)])
print(len(y))
#plan


#store all possible positions a move away.
#make_move(3,0,4,0,1, board, p1_2)
board_print(board)
def valid_next_positions(board):
  new_positions = valid_moves(p1_2, board)
  for key, value in new_positions.items():
    print(key[0])
    make_move(key[0], key[1], value[0], value[1], 1, board, p1_2)
valid_next_positions(board)
'''




