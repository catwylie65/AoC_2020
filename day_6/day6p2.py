from string import ascii_lowercase
file = open('day6.txt', 'r')

p = file.read().split('\n\n')

file.close()

total = 0

for group in p:
  counters = {}
  for letter in ascii_lowercase:
    counters[letter] = 0
  group = group.replace('\n', ' ')
  group = group.split(' ')
  for answers in group:
    for answer in answers:
      counters[answer] += 1

  for letter in counters.keys():
    if counters[letter] == len(group):
      total += 1

  # print(group)
  # print(len(group))

print(total)