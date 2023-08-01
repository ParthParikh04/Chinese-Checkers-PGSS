from legal_moves import *
import copy
import progressbar
from endgame_implementation import check_valid_endgame, make_endgame_move, my_flip_board

LEVELS_OF_SEARCH = 2 #Even number of layers I think??



'''
POSSIBLE BUGS
*************
- OverflowError in errors list :sob:
'''

def lookahead_pruning(p1, p2, board, level, best_val = -1 * MAX_CALCBOARD, calcboard=calc_board2, flipped=False): # returns the best value for any possible move
    # print("PRUNING")
    if level==0:
        # print_board(board)
        # score = calc_board3(p1, p2)
        score = calcboard(p1, p2)
        # print(score)
        # print(p1)
        # print(p2)
        # input()
        # print(f"Calculating board position and got {score}")
        return score
    else:
      # Flip the board and treat p1 and p2 as opposites here on out
      modified_board = copy.deepcopy(board)
      modified_p1 = copy.deepcopy(p1)
      modified_p2 = copy.deepcopy(p2)
      flip_board(modified_board, modified_p1, modified_p2)
      move_list = valid_moves(modified_p2, modified_board)
      # print("move_list in lookahead: ", end ="")
      # print(move_list)
      for key in move_list:
        for dest in move_list[key]:
          temp_board = copy.deepcopy(modified_board)
          temp_p1 = copy.deepcopy(modified_p1)
          temp_p2 = copy.deepcopy(modified_p2)
          player = 1 if temp_p2[10] == [0, 0] else 2
          make_move(key[0], key[1], dest[0], dest[1], player, temp_board, temp_p2)
          # print("fake move: ", key[0], key[1], dest[0], dest[1])
          # print(dest) # 1 or 2 subject to change
          # print_board(temp_board)
          if check_win(temp_board, 1 if player == 2 else 2, flipped=True):
            print("Check win returned true")
            return (MAX_CALCBOARD + 10) * -1 # I'm thinking we should do smthng like prof did and return a very extreme number here to account for  - Parth
          # print('CALLING LOOKAHEAD AGAIN')
          val = lookahead_pruning(temp_p1, temp_p2, temp_board, level-1, best_val, calcboard=calcboard) # Flip p1 and p2 to account for turn change (OR MAYBE NOT IDK???)
          # print(f"val: {val}")
          # print(f"Value from lookahead: {val}")
          if val > best_val:
            best_val = val
          else:
            return -(best_val)

      return -(best_val)


def lookahead(p1, p2, board, level, calcboard=calc_board1, flipped=False): # returns the best value for any possible move
    # print("NO PRUNING")
    if level==0:
        # score = calc_board3(p1, p2)
        score = calcboard(p1, p2)
        # print(f"Calculating board position and got {score}")
        return score
    else:
      # Flip the board and treat p1 and p2 as opposites here on out
      modified_board = copy.deepcopy(board)
      modified_p1 = copy.deepcopy(p1)
      modified_p2 = copy.deepcopy(p2)
      flip_board(modified_board, modified_p1, modified_p2)
      move_list = valid_moves(modified_p2, modified_board)
      # print("move_list in lookahead: ", end ="")
      # print(move_list)
      best_val = -1 * MAX_CALCBOARD
      for key in move_list:
        for dest in move_list[key]:
          temp_board = copy.deepcopy(modified_board)
          temp_p1 = copy.deepcopy(modified_p1)
          temp_p2 = copy.deepcopy(modified_p2)
          player = 1 if temp_p2[10] == [0, 0] else 2
          make_move(key[0], key[1], dest[0], dest[1], player, temp_board, temp_p2)
          # print("fake move: ", key[0], key[1], dest[0], dest[1])
          # print(dest) # 1 or 2 subject to change
          # print_board(temp_board)
          if check_win(temp_board, 1 if player == 2 else 2, flipped=True):
            print("Check win returned true")
            return (MAX_CALCBOARD + 10) * -1 # I'm thinking we should do smthng like prof did and return a very extreme number here to account for  - Parth
          # print('CALLING LOOKAHEAD AGAIN')
          val = lookahead(temp_p1, temp_p2, temp_board, level-1, calcboard=calcboard, flipped=flipped) # Flip p1 and p2 to account for turn change (OR MAYBE NOT IDK???)
          # print(val)
          # print(f"val: {val}")
          # print(f"Value from lookahead: {val}")
          if val > best_val:
            best_val = val

      return -(best_val)
          


def smartturn(board, level, p1, p2, lkahead = lookahead_pruning, pl = 0, clcbrd = calc_board2, flipped=False, endgame=True):
    print("STARTED SMART TURN")
    # Check endgame routine
    if endgame:
      if pl == 2:         
        new_board = my_flip_board(board)
      else:
        new_board = board

      if check_valid_endgame(new_board):
        move = make_endgame_move(new_board)
        if move != False:
          # print_board(new_board)
          # print(move)
          # input("Endgame")
          return move
  
    # If not an endgame routine, continue as normal  
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
          # if pl == 2:
          #   bool = not bool
          player = 1 if bool else 2 #player = 1 if we are p1 - originally is 1
          # print("PREMOVE: ", tempP1)
          # print(key)
          # print(dest)
          
          # Count 1s and 2s in board
          one = 0
          two = 0
          for row in tempBoard:
             for i in row:
                if i == 1:
                  one += 1
                elif i == 2:
                  two += 1

          # print("")
          # board_print(tempBoard)
          if(player ==1):
              # print(player)
              make_move(key[0], key[1], dest[0], dest[1], 2 if pl == 2 else player, tempBoard, tempP1)
          else:
              # print(player)
              make_move(key[0], key[1], dest[0], dest[1], 1 if pl == 2 else player, tempBoard, tempP2)

          # print(pl)

          # Count 1s and 2s in board
          one = 0
          two = 0
          for row in tempBoard:
             for i in row:
                if i == 1:
                  one += 1
                elif i == 2:
                  two += 1
          if one != two:
             print("ERROR: ONE AND TWO ARE NOT EQUAL")
             print_board(tempBoard)
             print(tempP1)
             print(tempP2)
             input()
          # input(": ")

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
          # print(mymove)
          if check_win(tempBoard, player):
              print("tempBoard: ")
              board_print(tempBoard)
              print_board(tempBoard)
              print(player)
              print("You win")
              print("ENDED SMART TURN")
              return (mymove)
              ## val = calcboard(tempBoard,mymove)
          
          # BOARD RIGHT BEFORE FIRST LOOKAHEAD
          # print("BOARD RIGHT BEFORE FIRST LOOKAHEAD")
          # print_board(tempBoard)
          val = lkahead(tempP1, tempP2, tempBoard,level, calcboard = clcbrd) #,mymove)
          # print("key: ",key, end="")
          # print("dest: ",dest)
          # print("value:", val)
          if val > bestval:
              bestval = val
              bestmove = copy.copy(mymove)
    # print ("bestval is ",bestval)
    # print("ENDED SMART TURN")
    return (bestmove)
  

# def smartturn(board, level, p1, p2):
#     movelist = valid_moves(p1, board)
#     if level == LEVELS_OF_SEARCH:
#       # random.shuffle(movelist)
#       pass
#     bestval = -1001
#     bestmove = []
#     for key in movelist:
#         for dest in movelist[key]: #for every possible move
#           tempBoard = copy.deepcopy(board)
#           bool = (p1[10] == [0, 0])  #tells us if we're p1 or p2
#           player = 2 if bool else 1 #player = 2 if we are p1
#           if bool:
#               print("FLIPPING BOARD")
#               flip_board(tempBoard, p1, p2)
#           make_move(key[0], key[1], dest[0], dest[1], 1, tempBoard, p1)
#           mymove = key[0], key[1], dest[0], dest[1]
#           if check_win(tempBoard, player):
#               print(tempBoard)
#               print(player)
#               print("you shouldn't be here yet")
#               return (mymove)
#               # val = calcboard(tempBoard,mymove)
#           val = lookahead(p1, p2, tempBoard,level) #,mymove)
#           if val > bestval:
#               bestval = val
#               bestmove = copy.copy(mymove)
#     # print ("bestval is ",bestval)
#     return (bestmove)



