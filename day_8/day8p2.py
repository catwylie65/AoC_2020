from collections import defaultdict 
import copy

file = open('input.txt', 'r')

lines = file.read().split('\n')

file.close()

instructions = defaultdict(list)
instructions_all = []

visited_instructions = []
saved = []

# get that data right
for index, line in enumerate(lines):
  instructions[index].append(line.split(' ')[0])
  instructions[index].append(line.split(' ')[1][0])
  instructions[index].append(line.split(' ')[1][1:])
last_index = len(instructions)
instructions[last_index].append('end')
instructions[last_index].append('+')
instructions[last_index].append('0')

def doThing(index, input):
  accumulator = 0
  instruction = input[index][0]
  positivity = input[index][1] == '+'
  value = int(input[index][2])
  if index in visited_instructions or instruction == 'end':
    if instruction == 'end':
        saved.clear()
        saved.append(input)
    return accumulator
  else:
    visited_instructions.append(index)

  if instruction == 'nop':
    accumulator = 0
    accumulator += doThing(index + 1, input)
  elif instruction == 'acc':
    if positivity:
      accumulator += value
    else:
      accumulator -= value
    accumulator += doThing(index + 1, input)
  else:
    if positivity: 
      accumulator += doThing(index + value, input)
    else:
      accumulator += doThing(index - value, input)
  saved.append(accumulator)
  return accumulator


# do something wit it
nop_index = []
jmp_index = []
for index, key in enumerate(instructions.keys()):
  if instructions[key][0] == 'nop':
    nop_index.append(index)
  if instructions[key][0] == 'jmp':
    jmp_index.append(index)

for index in jmp_index:
  new_thing = copy.deepcopy(instructions)
  new_thing[index][0] = 'nop'

  doThing(0, new_thing)
  visited_instructions = []

for index in nop_index:
  new_thing = copy.deepcopy(instructions)
  new_thing[index][0] = 'jmp'

  doThing(0, new_thing)
  visited_instructions = []

# print(saved)

print('accumulator =', doThing(0, saved[0]))