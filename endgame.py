import copy
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







  
      
    

#fucntion to convert from 2 player board to one player board
def convert_board(board):
  new_board = copy.deepcopy(board)
  M = 9
  for i in range(M):
    for j in range(M):
      if new_board[i][j] == 2:
        new_board[i][j] = 0
  return new_board 
        
#Check function

#x = make_board()
#board_print(x)
#y = convert_board(x)
#board_print(y)
  

#CREATE board position to store completed position
M = 9
finished_board = [[0 for i in range(M)] for j in range(M)]
for i in range(5,9):
  for j in range(13-i, 9):
    finished_board[i][j] = 1


#check finished board
#board_print(finished_board)




#Make function that changes board position from 2-d array to string   
#Note: This function reads left to right and then down, so top left square is first and bottom right square is last

def convert_board_to_string(board):
  M = 9
  board_string = ''
  for j in range(M):
    for i in range(M):
      board_string += str(board[i][j])
  return(board_string)



#test string conversion

#string = convert_board_to_string(finished_board)
#print(string)

#Make function to convert string back to board


def convert_string_to_board(s):
  M = 9
  board = [[0 for i in range(M)] for j in range(M)]
  for k in range(len(s)):
    char = int(s[k])
    i = k % 9
    j = int(k / 9)
    board[i][j] = char
  return(board)  

#test

print(convert_string_to_board(convert_board_to_string(finished_board)))

# Make dictionary for board positions
#Key will be string representation of position
#Value will be number of moves to completion


endgame_dictionary = dict()

#append string of finished position to dictionary with value 0

finished_string = convert_board_to_string(finished_board)

endgame_dictionary[finished_string] = 0

#check

#print(endgame_dictionary)

#get_p1 is a function that takes a board position and returns p1


def get_p1(board):
  M = 9
  p1 = []
  for i in range(M):
    for j in range(M):
      if board[i][j] == 1:
        p1.append([i,j])
  p1.append([0,0])
  return p1

'''def get_p2(board):
  M = 9
  p2 = []
  for i in range(M):
    for j in range(M):
      if board[i][j] == 2:
        p2.append([i,j])
  p2.append([8,8])
  return p2 '''
#test

#pieces = get_p1(finished_board)
#print(pieces)

#Note this function can be modified to generate both players pieces on a board

#NOTE for future, if program is running to slow I'll have to make my own make move function that uses the string form and doesn't convert

#Make function that stores all the possible next positions in the dictionary for a given start position


# Input of the function will be a string of the position and the number of moves away the string is. Hopefully we can loop through the dictionary 
# and use the keys and values of the dictionary to put in our positions

#Make a function that takes a board and dictionary of valid moves and returns all the valid new positions 


  

def new_positions(s_position,moves_away):
  board = convert_string_to_board(s_position) # Hopefully this get rid of having to make a copy, but copying might still be an issue.
  pieces = get_p1(board)
  #check
  #board_print(board)
  #print(pieces)
  new_moves = valid_moves(pieces,board)
  player = 1
  possible_positions = []
  for key in new_moves:
    value = new_moves[key]
    for end_position in value:
      new_pieces = copy.deepcopy(pieces)
      new_board = copy.deepcopy(board)  
      x1 = key[0]
      y1 = key[1]
      x2 = end_position[0]
      y2 = end_position[1]
      make_move(x1, y1, x2, y2, player, new_board, new_pieces)
      possible_positions.append(new_board)
#test
  #i= 0
  #for board in possible_positions:
   # board_print(board)
    #i += 1
    #print(i) 
# change positions back to strings
  s_possible_positions = []
  for position in possible_positions:
    s_possible_positions.append(convert_board_to_string(position))
  #print(s_possible_positions)
  for position in s_possible_positions:
    if position in endgame_dictionary:
      pass
    else:
      endgame_dictionary[position] = moves_away + 1
        
  




moves_out = 1
for moves_out in range(0,4):
  for position in copy.deepcopy(endgame_dictionary):
    if endgame_dictionary[position] == moves_out:
      new_positions(position,moves_out)

print(endgame_dictionary)
print(len(endgame_dictionary))