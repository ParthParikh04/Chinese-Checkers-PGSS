from endgame import*
from board import*
from legal_moves import*
import copy

#Check_in_endgame finds player 1s least advanced piece and checks if it is past player2s farthest advanced piece.
#The function should reutrn true if the position is an endgame

def check_in_endgame(board):
  player1_shortest = 10000
  player2_farthest = -16
  M = 9
  for i in range(M):
    for j in range(M):
      if board[i][j] == 1:
        if (i+j) <= player1_shortest:
          player1_shortest = (i+j)
  for i in range(M):
    for j in range(M):
      if board[i][j] == 2:
        if (i+j) >= player2_farthest:
          player2_farthest = (i+j)
  #check
  #print(player1_shortest)
  #print(player2_farthest)
  if player1_shortest > player2_farthest:
    return True
  else:
    return False



#check the function
#test_board = [[0 for i in range(M)] for j in range(M)]
#test_board[3][4] = 2
#test_board[3][3] = 1
#result = check_in_endgame(test_board)
#print(result)



#NOW make check_database to see if player1 is in a position stored in the database
def check_database(board):
  #convert board to only player 1
  x = copy.deepcopy(board)
  only_p1_board = convert_board(x)
  #convert board to string
  y = copy.deepcopy(only_p1_board)
  s_board = convert_board_to_string(y)
  #check
  #print(s_board)
  #check if string is in endgame_dictionary
  if s_board in endgame_dictionary:

    return True
  else:
    return False


#Check function

#result = check_database(finished_board)
#print(result)
#board = make_board()
#result2 = check_database(board)
#print(result2)


# MAKE function that combines above functions into one to check if a position is an endgame and is in the database

def check_valid_endgame(board):
  if check_in_endgame(board) == True:
    if check_database(board) == True:
      return True
    else:
      return False
  else:
    return False




#Check function



#Make function to make a move in the endgame by checking all the valid next positions and making the move to a position 
#one less away





#I have an error in my get_p1 function
#changing here

def real_get_p1(board):
  M = 9
  p1 = []
  for i in range(M):
    for j in range(M):
      if board[i][j] == 1:
        p1.append([j,i])
  p1.append([0,0])
  return p1



def make_endgame_move(board):
  #Make copy for later
  move_info_board = copy.deepcopy(board)
  #Take away player2's pieces
  x = copy.deepcopy(board)
  new_board = convert_board(x)
  #Get player 1s pieces
  pieces = real_get_p1(new_board)
  #test
  print(pieces)
#find all valid moves from new_board 
  valid_next_moves = valid_moves(pieces,new_board)
#Store all the valid next positions in an array
# This code is copyed from the function in endgame doing a similar thing
  player = 1

  possible_positions = []
  move_info_list = []
  
  for key in valid_next_moves:
    value = valid_next_moves[key]
    for end_position in value:
      new_pieces = copy.deepcopy(pieces)
      copy_pieces = copy.deepcopy(pieces)
      updated_board = copy.deepcopy(new_board)
      move_info = []
      #test
      #board_print(updated_board)
      x1 = key[0]
      y1 = key[1]
      x2 = end_position[0]
      y2 = end_position[1]
      move_info.append(x1)
      move_info.append(y1)
      move_info.append(x2)
      move_info.append(y2)
      move_info.append(player)
      move_info.append(board) # Note this is the real board be careful
      move_info.append(copy_pieces)
      #test
      #print(move_info)

      #append move info to move_info_list

      move_info_list.append(move_info)
      
      print(x1)
      print(y1)
      print(x2)
      print(y2)
      print(player)
      #board_print(updated_board)
      print(new_pieces)
      make_move(x1, y1, x2, y2, player, updated_board, new_pieces)
      board_print(updated_board)
      #test
      #board_print(updated_board)
      #Convert to string
      updated_board2 = copy.deepcopy(updated_board)
      #test
      
      final_board = convert_board_to_string(updated_board2)
      possible_positions.append(final_board)

  #print(possible_positions)    
# Now find which of the possible positions is one move away from the original position
  #check 

  z = copy.deepcopy(board)
  s_current_board = convert_board_to_string(convert_board(z))
  moves_away = endgame_dictionary[s_current_board]
  #check
  print(moves_away)
  if moves_away == 0:
    print("We won")
    return True
  for position in possible_positions:
    #Check
    #print(endgame_dictionary[position])
    n = endgame_dictionary.get(position, -10)
    print(n)
    if n == (moves_away-1):
      idx = possible_positions.index(position,0,len(possible_positions))
      print("")
      print(move_info[0])
      print(move_info[1])
      print(move_info[2])
      print(move_info[3])
      print(move_info[4])
      print(move_info[5])
      print(move_info[6])
      my_move = move_info_list[idx]
      return my_move[0],my_move[1],my_move[2], my_move[3]
      make_move(my_move[0],my_move[1],my_move[2], my_move[3], my_move[4],my_move[5],my_move[6])
      print("hello")
      print("")
      board_print(board)
      return True

  #If the function doesn't find a move return False
  return False



#Check
test_board = convert_string_to_board('000000000000000000000000000000000000000000000000000101000000111000000011000000111')
board_print(test_board)
pieces = real_get_p1(test_board)
print(pieces)
make_endgame_move(test_board)
make_endgame_move(test_board)
make_endgame_move(test_board)
#board_print(convert_string_to_board('000000000000000000000000000000000000000000000000000101000000111000000011000000111'))
























def smartturn(board, level, p1, p2):
    org_movelist = valid_moves(p1, board)
    # print("org_movelist: ", end ="")
    # print(org_movelist)
    movelist = dict()
    if level == LEVELS_OF_SEARCH:
      keys = list(org_movelist.keys()) #list of positions of pieces on board
      print(keys)
      random.shuffle(keys)
      
      for key in keys:
        random.shuffle(org_movelist[key]) 
        movelist[key] = org_movelist[key] 
    else:
      movelist = org_movelist
    bestval = -1001
    bestmove = []
    for key in movelist:
        for dest in movelist[key]: #for every move 
          tempBoard = copy.deepcopy(board)
          tempP1 = copy.deepcopy(p1)
          tempP2 = copy.deepcopy(p2)
          bool = (tempP1[10] == [0, 0])  #tells us if we're p1 or p2 - originally is true
          player = 1 if bool else 2 #player = 1 if we are p1 - originally is 1
          # print("PREMOVE: ", tempP1)
          # print(key)
          # print(dest)
          make_move(key[0], key[1], dest[0], dest[1], 1, tempBoard, tempP1)
          # print("fake move: ", key[0], key[1], dest[0], dest[1])
          # print("POSTMOVE: ", tempP1)
          if bool:
              # print("FLIPPING BOARD")
              # flip_board(tempBoard, tempP1, tempP2)
            pass
          # print("PREMOVE: ", tempP2)
          # make_move(key[0], key[1], dest[0], dest[1], 2, tempBoard, tempP2)
          # print("POSTMOVE: ", tempP2)
          mymove = key[0], key[1], dest[0], dest[1]
          if check_win(tempBoard, player):
              print("tempBoard: ")
              board_print(tempBoard)
              print(player)
              print("You win")
              return (mymove)
              ## val = calcboard(tempBoard,mymove)
          
          # BOARD RIGHT BEFORE FIRST LOOKAHEAD
          # print("BOARD RIGHT BEFORE FIRST LOOKAHEAD")
          # print_board(tempBoard)
          val = lookahead(tempP1, tempP2, tempBoard,level) #,mymove)
          # print("key: ",key, end="")
          # print("dest: ",dest)
          # print("value:", val)
          if val > bestval:
              bestval = val
              bestmove = copy.copy(mymove)
    # print ("bestval is ",bestval)
    return (bestmove)