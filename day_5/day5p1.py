import numpy as np
file = open('day5.txt', 'r')

seats = file.read().split('\n')

file.close()

highest_taken_seat = 0

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
  seat_id = (seat_row[0] * 8) + seat_column[0]
  if seat_id > highest_taken_seat:
    highest_taken_seat = seat_id

print(highest_taken_seat)

