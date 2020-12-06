file = open('2015-1.txt', 'r')

floors = file.read()

file.close()

floor = 0
basement = 0

for index, paren in enumerate(floors):
  if paren == '(':
    floor += 1
  else:
    floor -= 1
  
  if floor < 0:
    basement = index + 1
    break

print(basement)