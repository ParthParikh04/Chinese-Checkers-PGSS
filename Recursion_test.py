import random
# This is a test space for the recursive function
print("hello")
current_position = 1
level = 3
positions = []
def possible_moves(position):
  positions.append(current_position)
  for i in range(1,level):
    
  for i in rangenew_moves = []
  for i in range(1,5):
    new_moves.append(position+i)
    new_moves.append(position-i)
  return(new_moves)

moves = possible_moves(current_position)
print(moves)
for i in range(len(moves)):
  possible_moves(moves[i])
  
    
