

import numpy as np

# origin at top left

import math

def make_board():
    M = 9
    board = [[0 for i in range(M)] for j in range(M)]
    for i in range(4):
        for j in range(4-i):
            board[i][j] = 1
    for i in range(5,9):
        for j in range(13-i, 9):
            board[i][j] = 2
    return board

#Giving board coordinates 
def convert_board(square):
  if square == 0:
    print (" - ", end ='')
    
  if square == 1:
    print(" B ", end='')
    
  if square == 2:
    print(" R ", end='')
      board[i][j] = 2


def print_board(board):
  print ("  1  2  3  4  5  6  7  8  9")
  for i in range (len(board)):
    print(i + 1, end = '')
    for j in range(len(board[0])):
      if board[i][j] == 0:
        print (" - ", end ='')
      if board[i][j] == 1:
        print(" P ", end='')
      if board[i][j] == 2:
        print(" L ", end='')
  
    print("")


  
#Get valid user input 
def get_og_position():
  og_spot = str(input("Which piece would you like to move? "))
  if len(og_spot) == 2:
    y1 = og_spot[0]
    x1 = og_spot[1]
    if y1 in ('ABCDEFGHI') and x1 in ('123456789'):
      return(y1, x1)
  else:
    print("That is not a valid coordinate.")
    return get_og_position()

def get_new_position():
  new_spot = str(input("Where would you like to move your piece? "))
  if len(new_spot) == 2:
    y2 = new_spot[0]
    x2 = new_spot[1]
    if y2 in ('ABCDEFGHI') and x2 in ('123456789'):
      return(y2, x2)
  else:
    print("That is not a valid coordinate.")
    return get_new_position()

# #Store user input 
# og_position = (get_og_position())
# y1 = og_position[0]
# x1 = og_position[1]

# new_position = (get_new_position())
# y2 = new_position[0]
# x2 = new_position[1]

# print(y1, x1, y2, x2)






        