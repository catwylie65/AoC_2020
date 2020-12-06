import numpy as np
file = open('day5.txt', 'r')

seats = file.read().split('\n')

file.close()

the_plane = [['0' for num in range(8)] for num in range(128)]

for seat in seats:
  seat_row = [num for num in range(128)] # can be from 0-127
  seat_column = [num for num in range(8)] # can be from 0-7
  for fblr in seat:
    if fblr == 'F':
      seat_row = np.array_split(seat_row, 2)[0]
    elif fblr == 'B':
      seat_row = np.array_split(seat_row, 2)[1]
    elif fblr == 'L':
      seat_column = np.array_split(seat_column, 2)[0]
    else: # R
      seat_column = np.array_split(seat_column, 2)[1]
  the_plane[seat_row[0]][seat_column[0]] = 'X'

final_row = 0
final_column = 0
for index_row, row in enumerate(the_plane):
  for index, seat in enumerate(row):
    if seat == '0':
      if index - 1 > -1 and row[index - 1] == 'X': 
        if index + 1 < len(row) and row[index + 1] == 'X':
          final_row = index_row
          final_column = index
  
seat_id = (final_row * 8) + final_column
print(seat_id)
