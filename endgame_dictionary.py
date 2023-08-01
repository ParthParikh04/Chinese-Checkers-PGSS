import pickle
def load_in_table():
  endgame_table = pickle.load(open("end_table.txt", "rb"))
  return endgame_table
#endgame_table = load_in_table()
#print(endgame_table)