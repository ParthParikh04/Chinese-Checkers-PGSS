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
  
board = make_board()

#Confirm position
def confirm_position
  answer = str(input("Would you like to move", y1, x1, "? Enter 0   to confirm your move or 1 to cancel your move." 
    if answer == 0
      print("Your move", y1, x1, "has been confirmed.")  
    elif answer == 1
      print("Your move", y1, x1, "has been canceled.")  


#print(board)
#for i in range (len(board)):
  #for j in range(len(board[0])):
    #print(board[i][j], end=' ')
  #print("")

#Giving board coordinates 
def convert_board(square):
  if square == 0:
    print (" - ", end ='')
    
  if square == 1:
    print(" B ", end='')
    
  if square == 2:
    print(" R ", end='')

def print_board(board):
  print ("  A  B  C  D  E  F  G  H  I")
  for i in range (len(board)):
    print(i + 1, end = '')
    for j in range(len(board[0])):
      print(convert_board(board[i][j]))
    print("")

#print_board(board)
    
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
  new_spot = str(input("Enter where you would like to move: "))
  if len(new_spot) == 2:
    y2 = new_spot[0]
    x2 = new_spot[1]
    if y2 in ('ABCDEFGHI') and x2 in ('123456789'):
      return(y,x)
  else:
    print("That is not a valid coordinate.")
    return get_position()


'''import numpy as np

# origin at top left

import math

def print_square(square):
  M = 9
  board = [[0 for i in range(M)] for j in range(M)]
  for i in range(4):
    for j in range(4-i):
        board[i][j] = 1
  for i in range(5,9):
      for j in range(13-i, 9):
         board[i][j] = 2
  #print(board)
  
  print ("  1  2  3  4  5  6  7  8  9")
  for i in range (len(board)):
    print(i + 1, end = '')
    for j in range(len(board[0])):
      print_square(board[i][j])
  
    print("")
  if square == 0:
    print (" - ", end ='')
  if square == 1:
    print(" P ", end='')
  if square == 2:
    print(" L ", end='')

   


#for i in range(len(board)):
  #for j in range(len(board[0])):
    #if board[i][j] == 1:
      #print("+")
    #if board[i][j] == 2:
      #print("-")
    #if board[i][j] == 0:

#def make_move(x1, y1, x2, y2, team):
  #board[x1][y1] = 0
  #board[x2][y2] = team
  #print(board)
'''

