from endgame_dictionary import *
from endgame_implementation import *
from board import *

#Make test board

M = 9
test_board = [[0 for i in range(M)] for j in range(M)]
#player 1 positions
test_board[8][8] = 1
test_board[8][7] = 1
test_board[7][8] = 1
test_board[7][7] = 1
test_board[8][6] = 1
test_board[6][8] = 1
test_board[8][5] = 1
test_board[4][8] = 1
test_board[7][6] = 1
test_board[6][7] = 1
#player 2 positions
test_board[0][8] = 2
test_board[1][7] = 2
test_board[7][1] = 2
test_board[6][2] = 2
test_board[5][3] = 2
test_board[3][5] = 2
test_board[4][5] = 2
test_board[3][3] = 2
test_board[5][2] = 2
test_board[4][2] = 2


board_print(test_board)
print(check_in_endgame(test_board))
print(check_database(test_board))
make_endgame_move(test_board)