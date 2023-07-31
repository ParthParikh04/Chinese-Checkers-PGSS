

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
# def convert_board(square):
#   for i in range(9):
#     for j in range(9):
#       #print(board[i][j], end=' ')
#     #print("")
#   # if square == 0:
#   #   print (" - ", end ='')
    
#   # if square == 1:
#   #   print(" P ", end='')
    
#   # if square == 2:
#   #   print(" L ", end='')

#Printing board 
def print_board(board):
  print ("  A  B  C  D  E  F  G  H  I")
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



#Convert user input y from letter to number
def convert_letter_to_num(x):
  for character in x:
    number = ord(character) - 65
  return number

#Get valid user input for old and new position 
def get_og_position():
  og_spot = str(input("Which piece would you like to move? ")).upper()
  if len(og_spot) == 2:
    x1 = int(convert_letter_to_num(og_spot[0]))
    y1 = int(og_spot[1]) - 1
    return(x1, y1)
  else:
    print("That is not a valid coordinate.")
    return get_og_position()

def usr_change_piece():
  poss_change = str(input("If you would like to move somewhere else select 1. If you would like to select a new piece to move, enter 0. "))
  return poss_change
  

def get_new_position():
  new_spot = str(input("Where would you like to move your piece? "))
  if len(new_spot) == 2:
    x2 = int(convert_letter_to_num(new_spot[0]))
    y2 = int(new_spot[1]) - 1
    return(x2, y2)
  else:
    print("That is not a valid coordinate.")
    print(new_spot)
    return get_new_position()

def continue_move():
  cont = str((input("Would you like to continue jumping? Enter 2 for YES and 3 for NO: ")))
  return cont
    
    

