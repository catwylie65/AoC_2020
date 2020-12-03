with open('day_3.txt', 'r') as f:
  landscape = [[c for c in line.split('\n')[0]] for line in f]

# remember l[down][across]
# len of row = 31
current_down = 0
current_across = 0

trees_1 = 0
trees_2 = 0
trees_3 = 0
trees_4 = 0
trees_5 = 0

# Right 1 down 1 (WORKS) (trees_1)
for row in landscape:
  if row[current_across] == '#':
    trees_1 += 1

  current_across += 1
  if current_across > len(landscape[0]) - 1:
    current_across = current_across - len(landscape[0])

current_across = 0

# Right 3 down 1 (WORKS) (trees_2)
for row in landscape:
  if row[current_across] == '#':
    trees_2 += 1

  current_across += 3
  if current_across > len(landscape[0]) - 1:
    current_across = current_across - len(landscape[0])

current_across = 0

# Right 5 down 1 (WORKS) (trees_3)
for row in landscape:
  if row[current_across] == '#':
    trees_3 += 1

  current_across += 5
  if current_across > len(landscape[0]) - 1:
    current_across = current_across - len(landscape[0])
current_across = 0

# Right 7 down 1 (trees_4) (WORKS)
for row in landscape:
  if row[current_across] == '#':
    trees_4 += 1

  current_across += 7
  if current_across > len(landscape[0]) - 1:
    current_across = current_across - len(landscape[0])
current_across = 0

# Right 1 down 2 (trees_5)
for row in landscape:
  if current_down % 2 != 0: 
    current_down += 1
    continue
  if row[current_across] == '#':
    trees_5 += 1

  current_across += 1
  current_down += 1
  if current_across > len(landscape[0]) - 1:
    current_across = current_across - len(landscape[0])

print('Trees 1: ', trees_1)
print('Trees 2: ', trees_2)
print('Trees 3: ', trees_3)
print('Trees 4: ', trees_4)
print('Trees 5: ', trees_5)

print(trees_1*trees_2*trees_3*trees_4*trees_5)
# 1675950276 is too low