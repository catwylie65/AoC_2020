from collections import defaultdict 

file = open('input.txt', 'r')

lines = file.read().split('\n')

file.close()

instructions = defaultdict(list)
visited_instructions = []

# get that data right
for index, line in enumerate(lines):
  instructions[index].append(line.split(' ')[0])
  instructions[index].append(line.split(' ')[1][0])
  instructions[index].append(line.split(' ')[1][1:])

def doThing(index):
  accumulator = 0
  if index in visited_instructions:
    return accumulator
  else:
    visited_instructions.append(index)
  instruction = instructions[index][0]
  positivity = instructions[index][1] == '+'
  value = int(instructions[index][2])
  if instruction == 'nop':
    accumulator = 0
    accumulator += doThing(index + 1)
  elif instruction == 'acc':
    if positivity:
      accumulator += value
    else:
      accumulator -= value
    accumulator += doThing(index + 1)
  else:
    if positivity: 
      accumulator += doThing(index + value)
    else:
      accumulator += doThing(index - value)
  return accumulator


# do something wit it
# for key in instructions.keys():
#   print(key, instructions[key])
print('accumulator =', doThing(0))