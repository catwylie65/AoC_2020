file = open('day6.txt', 'r')

p = file.read().split('\n\n')

file.close()

total = 0
for line in p:
  data = line.replace('\n', '')
  no_dups = "".join(set(data))
  total += len(no_dups)

print(total)