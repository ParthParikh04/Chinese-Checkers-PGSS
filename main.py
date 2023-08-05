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
from smart_turn import smartturn
from legal_moves import flip_board
import sys



#Make starting board
board = make_board()
print_board(board)
print("You are player L for Loser >:D")


#Put starting values in board
M = 9
p1 = []
p2 = []
board = [[0 for i in range(M)] for j in range(M)]
count = 0
for i in range(4):
  for j in range(4 - i):
    board[i][j] = 1
    p1.append([i, j])
    count = count + 1


# Store origin of player 1's pieces as the last element of p1
p1.append([0, 0])

count = 0
for i in range(5, 9):
  for j in range(13 - i, 9):
    board[i][j] = 2 
    p2.append([i, j])
    count += 1
board_print(board)
# Store origin of player 2's pieces as the last element of p2
p2.append([8, 8])


# sys.exit()

#Get coordinates of piece that human would like to move
player = 2
x1, y1 = get_og_position()

#Check validity of og position and update
while curr_validity_check(x1, y1, board) == False or check_human_is_plyr_2(x1, y1, board) == False:
  print('Sorry, that is not valid. Please try again.')
  x1, y1 = get_og_position()
      
#Check and get validity of new move 
x2, y2 = get_new_position()
      
#Check validity of new move and allow change of move or peg.
while validity_check(board, x1, y1, x2, y2) == False:
  print('Sorry, that is not a valid move. Please try again.')
  change_piece = usr_change_piece()
  if int(change_piece) == 0:
    x1, y1 = get_og_position()
    #print('y', y1, 'x', x1, curr_validity_check(x1, y1, board))
    while curr_validity_check(x1, y1, board) == False or check_human_is_plyr_2(x1, y1, board) == False:
      print('Sorry, that is not valid. Please try again.')
      x1, y1 = get_og_position()
    x2, y2 = get_new_position()
  elif int(change_piece) == 1:
    x2, y2 = get_new_position()
  else:
    print('no move')
    break


make_move(x1, y1, x2, y2, player, board, p2)
print_board(board)

board_print(board)

# Computer makes a move
#print('p2', p2)

player = 1

# Code for random turn
# y1, x1, y2, x2 = random_turn(board, player, p1)

# Code for smartturn
flip_board(board, p1, p2)
x1, y1, x2, y2 = smartturn(board, 5, p1, p2, pl=2, clcbrd=calc_board4)
make_move(x1, y1, x2, y2, player, board, p1)
flip_board(board, p1, p2)

print_board(board)


#Loop for players
player = 2
cont = 0
#print(check_win(board) == False)
#Check for win.
while check_win(board) == False:
  #Human move player 2
    # print('p1', p1)
    # print('p2', p2)
    #board_print(board)
    if player == 2:

      x1, y1 = get_og_position()
      
      #Check validity of og position and update
      while curr_validity_check(x1, y1, board) == False or check_human_is_plyr_2(x1, y1, board) == False:
        #print('curr', curr_validity_check(x1, y1, board), 'human', check_human_is_plyr_2(x1, y1, board))
  
        print(' Sorry, that is not valid. Please try again.')
        x1, y1 = get_og_position()
            
      #Check validity of new move 
      x2, y2 = get_new_position()
            
      #Check validity of new move and allow change of move or peg.
      while validity_check(board, x1, y1, x2, y2) == False:
        print(' Sorry, that is not a valid move. Please try again.')
        change_piece = usr_change_piece()
        if int(change_piece) == 0:
          x1, y1 = get_og_position()

          #print(y1, x1, curr_validity_check(x1, y1, board))
          while curr_validity_check(x1, y1, board) == False or check_human_is_plyr_2(x1, y1, board) == False:
            print(' Sorry, that is not valid. Please try again.')
            x1, y1 = get_og_position()
          x2, y2 = get_new_position()
        elif int(change_piece) == 1:
          x2, y2 = get_new_position()
        else:
          print('no move')

      make_move(x1, y1, x2, y2, player, board, p2)
      print_board(board)

      #Allow player to continue moving the piece
      while True:
        try:
          cont = int(continue_move())
          break
        except ValueError:
          print("Invalid input. Try again!")
          
      while cont == 2:
        x1, y1 = x2, y2
        x2, y2 = get_new_position()
        if jump_validity_check(board, x1, y1, x2, y2) == True:
          make_move(x1, y1, x2, y2, player, board, p1)
          print_board(board)
        else:
          print('Sorry, that is not a valid move. Please try again.')
        cont = int(continue_move())
      else:
        player -= 1
      
    #Computer move player 1
    elif player == 1:
      # Code for random turn
      # y1, x1, y2, x2 = random_turn(board, player, p1)
      
      # Code for smartturn
      flip_board(board, p1, p2)
      x1, y1, x2, y2 = smartturn(board, 5, p1, p2, pl=2, clcbrd=calc_board4)
      make_move(x1, y1, x2, y2, player, board, p1)
      flip_board(board, p1, p2)
      
      #print("Update p1")
      print_board(board)

      player += 1
      


print('DONE SOMEONE WON YAY')