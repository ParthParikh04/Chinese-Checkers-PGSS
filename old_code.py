def valid_moves(pieces, single_move): # subject to change if we want to combine the 1-block move and 2-block move in a single function
  valid = dict()
  for piece in pieces:
    valid[piece] = list()
    for i in range(0, 8):
      x_inc = [0, 0, 0, 0, -2, -1, 2, 1]
      y_inc = [-2, -1, 2, 1, 0, 0, 0, 0]
      new_loc = [piece[0] + y_inc[i], piece[1] + x_inc[i]]
      try:
        board[new_loc[0]][new_loc[1]]
      except IndexError:
        continue

      if validity_check(piece[0], piece[1], new_loc[0], new_loc[1]): [piece].append(new_loc)


# Always returned true
def check_win(pieces):  #pieces is p1 or p2
  if pieces[10] == [0, 0]:
    destinations = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2],
                    [2, 0], [2, 1], [3, 0]]
  elif pieces[10] == [8, 8]:
    destinations = [[5, 8], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 5],
                    [8, 6], [8, 7], [8, 8]]
  else:
    return False

  for dest in destinations:
    if dest not in pieces:
      return False

  return True