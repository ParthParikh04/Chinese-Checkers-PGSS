import numpy as np
# from board import *
import pprint
import copy

# origin at top left

import math
import statistics
import random
from board import *
import time

# M = 9
# p1 = []
# p2 = []
# board = [[0 for i in range(M)] for j in range(M)]
# count = 0
# for i in range(4):
#   for j in range(4 - i):
#     board[i][j] = 1
#     p1.append([i, j])
#     count = count + 1

# # Store origin of player 1's pieces as the last element of p1
# p1.append([0, 0])

# count = 0
# for i in range(5, 9):
#   for j in range(13 - i, 9):
#     board[i][j] = 2
#     p2.append([i, j])
#     count += 1

# # Store origin of player 2's pieces as the last element of p2
# p2.append([8, 8])


def board_print(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print("")


# ## NOTE I GOT RID OF P1 AND P2 SWITCH IN HERE GUYS
# def flip_board(board, p1, p2):
#     for piece in p1[:-1]:
#       board[piece[1]][piece[0]] = 0
#     for piece in p2[:-1]:
#       board[piece[1]][piece[0]] = 0
#     temp = copy.deepcopy(p1)
#     p1 = copy.deepcopy(p2)
#     p2 = temp

#     for piece in p1:
#         board[piece[1]][piece[0]] = 1
#     for piece in p2:
#         board[piece[1]][piece[0]] = 2


def flip_board(board, p1, p2):
    for piece in p1[:-1]:
        board[piece[1]][piece[0]] = 0
    for piece in p2[:-1]:
        board[piece[1]][piece[0]] = 0

    for i in range(len(p1)):
        p1[i][0] = 8 - p1[i][0]
        p1[i][1] = 8 - p1[i][1]
        p2[i][0] = 8 - p2[i][0]
        p2[i][1] = 8 - p2[i][1]
    

    for piece in p1[:-1]:
        board[piece[1]][piece[0]] = 1
    for piece in p2[:-1]:
        board[piece[1]][piece[0]] = 2


def make_move(x1, y1, x2, y2, player, board, pieces):
    #player is either 1 or 2
    # print('plyr', player)
    # print('pie', pieces)
    '''
  print("IN MAKE MOVE")
  print(x1, y1, x2, y2)
  print(pieces)
  '''
    # print("IN MAKE MOVE")
    # print(x1, y1, x2, y2)

    try:
        ind = pieces.index([x1, y1])
    except ValueError:  #check if this error is right for a dictionary
        # print("OUT MAKE MOVE")
        return False

    # Update if no errors
    board[y1][x1] = 0
    board[y2][x2] = player
    pieces[ind] = [x2, y2]
    # print(pieces)
    # '''if player == 2:
    #   try:
    #     ind = p2.index([y1, x1])
    #   except ValueError:
    #     return False
    #   p2[ind] = [y2, x2]'''
    # print("OUT MAKE MOVE")


#fix it so that it's a try catch and uses index instead of find


def curr_validity_check(x1, y1, board):
    #print('y', y1, 'x', x1)
    #print(board[y1][x1])
    if x1 < 0 or x1 > 9 or y1 < 0 or y1 > 9:
        # print('1')
        return False
    if board[y1][x1] > 0:
        return True
    return False


#Check if right player
def check_human_is_plyr_2(x1, y1, board):
    if board[y1][x1] == 2:
        return True
    return False


#Check the validity of a given move
def validity_check(board, x1, y1, x2, y2):
    if x1 < 0 or x1 > 9 or x2 < 0 or x2 > 9 or y1 < 0 or y1 > 9 or y2 < 0 or y2 > 9:
        # print('1')
        return False

    elif board[y2][x2] != 0:
        # print('22')
        return False

    elif abs(y1 - y2) == 2 and x1 == x2:
        # print('3')
        return (board[int((y1 + y2) / 2)][x1] == 1 or board[int(
            (y1 + y2) / 2)][x1] == 2)

    elif abs(x1 - x2) == 2 and y1 == y2:
        # print('4')
        return (board[y1][int((x1 + x2) / 2)] == 1 or board[y1][int(
            (x1 + x2) / 2)] == 2)

    elif abs(x1 - x2) == 1 and y1 == y2:
        return True

    elif abs(y1 - y2) == 1 and x1 == x2:

        return True

    else:
        # print('7')
        return False


#Check the validity of only jumps
def jump_validity_check(board, x1, y1, x2, y2):
    if x1 < 0 or x1 > 9 or x2 < 0 or x2 > 9 or y1 < 0 or y1 > 9 or y2 < 0 or y2 > 9:
        # print('1')
        return False

    elif board[y2][x2] != 0:
        # print('22')
        return False

    elif abs(y1 - y2) == 2 and x1 == x2:
        # print('3')
        return (board[int((y1 + y2) / 2)][x1] == 1 or board[int(
            (y1 + y2) / 2)][x1] == 2)

    elif abs(x1 - x2) == 2 and y1 == y2:
        # print('4')
        return (board[y1][int((x1 + x2) / 2)] == 1 or board[y1][int(
            (x1 + x2) / 2)] == 2)

    else:
        # print('7')
        return False


def reset_board(board):
    for i in range(9):
        for j in range(9):
            if (board[i][j] >= 3):
                board[i][j] -= 3


def valid_chain(x1, y1, board):
    endings = []
    x_inc = [0, 0, -2, 2]
    y_inc = [-2, 2, 0, 0]
    for i in range(0, 4):
        x2 = x1 + x_inc[i]
        y2 = y1 + y_inc[i]
        #print([y2, x2])
        try:
            if board[y2][x2] >= 3:
                continue
        except IndexError:
            continue
        if board[y1][x1] < 3: board[y1][x1] += 3
        if validity_check(board, x1, y1, x2, y2):
            endings.append([x2, y2])
            endings += valid_chain(x2, y2, board)

    return endings


def valid_moves(pieces, board):
    # subject to change if we want to combine the 1-block move and 2-block move in a single function
    valid = dict()
    for piece in pieces[:-1]:
        valid[tuple(piece)] = []
        #NEED TO KEEP THIS           FOR RANDOM_TURN DICTIONARY MERGE
        # Rolls
        x_inc = [0, 0, -1, 1]
        y_inc = [-1, 1, 0, 0]
        for i in range(0, 4):
            new_loc = [piece[0] + x_inc[i], piece[1] + y_inc[i]]
            try:
                board[new_loc[1]][new_loc[0]]
            except IndexError:
                continue
            if new_loc != [] and validity_check(board, piece[0], piece[1],
                                                new_loc[0], new_loc[1]):
                valid[tuple(piece)].append(new_loc)
#board[0][0]
# Jumps
        ls = valid_chain(piece[0], piece[1], board)
        # print("ls: ", ls)
        valid[tuple(piece)] += ls
        # Add list of rolls to valid[tuple(piece)]
        # Add output from call to valid_chain to valid[tuple(piece)]
        '''print('BEFORE RESET BOARD')
    print(board)'''
        reset_board(board)
        '''print('AFTER RESET BOARD')
    print(board)'''
        # print("valid moves: ", valid)
    return valid


#sample output: {(0, 0): [], (0, 1): [], (0, 2): [[2, 2], [0, 4]], (0, 3): [], (1, 0): [], (1, 1): [[3, 1], [1, 3]], (1, 2): [], (2, 0): [[4, 0], [2, 2]], (2, 1): [], (3, 0): []}


def random_turn(board, player, pieces):  # returns a random legal move
    #MERGE DICTIONARIES
    '''if player == 1:
    pieces = p1
  else:
    pieces = p2'''

    moves = valid_moves(pieces, board)  #prints
    ### print("valid moves: ", moves)
    '''
  Returns first element, to check other code if bug in random_turn
  i = 0
  while True:
    try:
      return list(moves.keys())[i][1], list(moves.keys())[i][0], moves[list(moves.keys())[i]][0][1], moves[list(moves.keys())[i]][0][0]
    except IndexError:
      i +=1
      pass
  '''

    # #print(moves)
    # moves_list = list(moves)
    # new_list = []
    # for key in moves_list:
    #   if moves[key] != []:
    #     new_list.append((key, moves[key]))

    # rand_piece = random.choice(list(new_list))
    # poss_moves = rand_piece[1]
    # rand_move_ind = random.randint(0, len(poss_moves) - 1)

    # y1 = rand_piece[0][0]
    # x1 = rand_piece[0][1]
    # y2 = poss_moves[rand_move_ind][0]
    # x2 = poss_moves[rand_move_ind][1]

    rand_num = random.randrange(0, 10)
    # b = pieces[rand_num]
    # print(b)
    # c = moves[tuple(b)]
    # print(c)
    p = pieces[rand_num]

    a = moves[tuple(p)]
    # print("here", a)
    while a == []:
        rand_num = random.randrange(0, 10)
        p = pieces[rand_num]
        a = moves[tuple(p)]
        # print("in loop: ", a)
    b = len(a)
    rand_1 = random.randrange(0, b)
    x2 = a[rand_1][0]
    y2 = a[rand_1][1]
    x1 = p[0]
    y1 = p[1]
    # print("here")

    return y1, x1, y2, x2


def check_win(board, player=1, flipped=False):  #pieces is p1 or p2
    win = False
    # player = 2 if player == 1 else 1
    if player == 2 and not flipped:
        for i in range(0, 4):
          for j in range(0, 4-i):
              if board[i][j] == player:
                  win = True
              if board[i][j] == 0:
                  return False
    else:
      for i in range(5, 9):
          for j in range(8 - i + 5, 9):
              if board[i][j] == player:
                  win = True
              if board[i][j] == 0:
                  return False
    return win


'''def check_win(board):
  return False'''


def calc_board1(pieces, pieces_opp):  #calculated from p1's point of view
    sum = 0
    for piece in pieces[:-1]:
        # print(piece)
        sum += piece[0]
        sum += piece[1]
    # print("sum: ", sum)
    return sum


# def calc_board(pieces): #calculated from origin's point of view
#     sum = 0
#     for piece in pieces[:-1]:
#         sum += piece[0]
#         sum += piece[1]
#     return sum



MAX_CALCBOARD = 999999


def calc_board2(pieces, pieces_opp):  #calculated from p1's point of view
    sum = 0
    for piece in pieces[:-1]:
        # print(piece)
        sum += (9 - piece[0]) * (9 - piece[0])
        sum += (9 - piece[1]) * (9 - piece[1])
    # print("sum: ", sum)
    return 1000 - sum  # score is 0 when starting, 960 when won


def calc_board3(pieces, pieces_opp, weight = 10):  #it seems like weight must be very large since the difference in standard deviation is not great.
    xs = []
    ys = []
    sum = 0
    for i in range(len(pieces)-1):
        xs.append(pieces[i][0] * 5)
        xs.append(pieces_opp[i][0])
        ys.append(pieces[i][1] * 5)
        ys.append(pieces_opp[i][0])
        sum += (9 - pieces[i][0]) * (9 - pieces[i][0])
        sum += (9 - pieces[i][1]) * (9 - pieces[i][1])

    stdev = statistics.stdev(xs) + statistics.stdev(ys)

    # print("********")
    # print(sum)
    # print(stdev * weight)
    # print (4000 - sum - stdev*weight)

    # print(10000 - sum - stdev * weight)

    return 10000 - sum - stdev * weight
    # return score / stdev # score is 0 when starting, 960 when won


def calc_board4(pieces, pieces_opp, diffs_weight=1):
  sum = 0
  diffs_weight 
  diffs = 0
  for piece in pieces[:-1]:
    # print(piece)
    sum += (9 - piece[0]) * (9 - piece[0])
    sum += (9 - piece[1]) * (9 - piece[1])
    diffs += abs(piece[0] - piece[1])

  # print(sum)
  # print(diffs * diffs_weight)
  return 10000 - sum - diffs * diffs_weight
  

#since we have the board now, if we really need to make check_win faster, we can. Good as is for now
