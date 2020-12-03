with open('day_3.txt', 'r') as f:
  landscape = [[c for c in line.split('\n')[0]] for line in f]

# remember l[down][across]
# len of row = 31
current_across = 0
trees = 0

for row in landscape:
  if row[current_across] == '#':
    row[current_across] = 'X'
    trees += 1
  if row[current_across] == '.':
    row[current_across] = '0'

  current_across += 3
  if current_across > len(landscape[0]) - 1:
    current_across = current_across - len(landscape[0])
  print(row)

print('Trees: ', trees)
